from flask import Flask, session, render_template, request, redirect, url_for
from .scraper import driver, filter
from .formatter import formatResult
import json
from .features import create_user, wishlist_add_item, read_wishlist, wishlist_remove_list

app = Flask(__name__, template_folder=".")

app.secret_key = 'asdsdfsdfs13sdf_df%&'


@app.route('/')
def landingpage():
    login = False
    if 'username' in session:
        login = True
    return render_template("./static/landing.html", login=login)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        create_user(request.form['username'])
        return redirect(url_for('login'))
    return render_template('./static/login.html')


@app.route('/wishlist')
def wishlist():
    username = session['username']
    wishlist_name = "default"
    items = read_wishlist(username, wishlist_name).to_dict('records')
    return render_template('./static/wishlist.html', data=items)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('./static/landing.html')


@app.route("/search", methods=["POST", "GET"])
def product_search(new_product="", sort=None, currency=None, num=None, min_price = None, max_price = None, min_rating = None):
    product = request.args.get("product_name")
    if product == None:
        product = new_product

    data = driver(product, currency, num, 0, False, None, True, sort)

    if min_price is not None or max_price is not None or min_rating is not None:
        data = filter(data, min_price, max_price, min_rating)

    return render_template("./static/result.html", data=data, prod=product)


@app.route("/filter", methods=["POST", "GET"])
def product_search_filtered():
    
    product = request.args.get("product_name")
    sort = request.form["sort"]
    currency = request.form["currency"]
    
    min_price = request.form["min_price"]
    max_price = request.form["max_price"]
    min_rating = request.form["min_rating"]

    try:
        min_price = float(min_price)
    except:
        min_price = None

    try:
        max_price = float(max_price)
    except:
        max_price = None

    try:
        min_rating = float(min_rating)
    except:
        min_rating = None

    if sort == "default":
        sort = None
    if currency == "usd":
        currency = None

    return product_search(product, sort, currency, None, min_price, max_price, min_rating)

@app.route("/add-wishlist-item", methods=["POST"])
def add_wishlist_item():
    username = session['username']
    item_data = request.form.to_dict()
    wishlist_name = 'default'
    wishlist_add_item(username, wishlist_name, item_data)
    return ""

@app.route("/delete-wishlist-item", methods=["POST"])
def remove_wishlist_item():
    username = session['username']
    index = int(request.form["index"]) 
    wishlist_name = 'default'
    wishlist_remove_list(username, wishlist_name, index)
    return redirect(url_for('wishlist'))

if __name__ == '__main__':
    app.run(debug=True)
