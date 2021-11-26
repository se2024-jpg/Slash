from flask import Flask, request, render_template
import scraper
import json

app = Flask(__name__, template_folder='.')

@app.route("/")
def landingpage():
    return render_template('./static/landing.html')

@app.route('/search', methods=['POST', 'GET'])
def product_search(new_product='', sort=None, currency=None, num=None):
    product = request.args.get('product_name')
    if product == None:
        product = new_product

    data = scraper.driver(product, currency, num, 0, False, None, True, sort)

    return render_template('./static/result.html', data=data)

@app.route('/filter', methods=['POST', 'GET'])
def product_search_filtered():

    ref = request.referrer.split("=")
    product = ref[1]
    sort = request.form['sort']
    currency = request.form['currency']
    num = request.form['num']

    if sort == 'default':
        sort = None
    if currency == 'default':
        currency = None 
    if num == 'default':
        num = None
    return product_search(ref[1], sort, currency, num)