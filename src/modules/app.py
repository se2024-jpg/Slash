from flask import Flask, session, render_template, request, redirect, url_for
from .scraper import driver, filter
import json
from .features import create_user

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
    return render_template('./static/wishlist.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('./static/landing.html')


@app.route("/search", methods=["POST", "GET"])
def product_search(new_product="", sort=None, currency=None, num=None, min_price = None, max_price = None):
    product = request.args.get("product_name")
    if product == None:
        product = new_product

    data = driver(product, currency, num, 0, False, None, True, sort)

    if min_price is not None or max_price is not None:
        data = filter(data, min_price, max_price)

    return render_template("./static/result.html", data=data, prod=product)


@app.route("/filter", methods=["POST", "GET"])
def product_search_filtered():
    
    product = request.args.get("product_name")
    rating_sort = request.form["rating_sort"]
    currency = request.form["currency"]
    num = request.form["num"]
    
    min_price = request.form["min_price"]
    max_price = request.form["max_price"]

    try:
        min_price = float(min_price)
    except:
        min_price = None

    try:
        max_price = float(max_price)
    except:
        max_price = None

    if rating_sort == "default":
        rating_sort = None
    if currency == "usd":
        currency = None
    if num == "default":
        num = None
    return product_search(product, rating_sort, currency, num, min_price, max_price)


if __name__ == '__main__':
    app.run(debug=True)
