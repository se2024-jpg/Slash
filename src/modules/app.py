from flask import Flask, session, render_template, request, redirect, url_for
from .scraper import driver
import json

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
        return redirect(url_for('login'))
    return render_template('./static/login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('./static/landing.html')


@app.route("/search", methods=["POST", "GET"])
def product_search(new_product="", sort=None, currency=None, num=None):
    product = request.args.get("product_name")
    if product == None:
        product = new_product

    data = driver(product, currency, num, 0, False, None, True, sort)

    return render_template("./static/result.html", data=data, prod=product)


@app.route("/filter", methods=["POST", "GET"])
def product_search_filtered():

    product = request.args.get("product_name")
    sort = request.form["sort"]
    currency = request.form["currency"]
    num = request.form["num"]

    if sort == "default":
        sort = None
    if currency == "usd":
        currency = None
    if num == "default":
        num = None
    return product_search(product, sort, currency, num)
