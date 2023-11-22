from src.modules import scraper
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))

def test_filter():
    data = [ {"price": "$10", "rating": "4.5"}, {"price": "$20", "rating": "4.0"}, {"price": "$30", "rating": "3.5"}, {"price": "$40", "rating": "5"} ]
    result = scraper.filter(data, 25, None, None)
    assert len(result) == 2
    result = scraper.filter(data, None, 35, None)
    assert len(result) == 3
    result = scraper.filter(data, None, None, 4.1)
    assert len(result) == 2

def test_driver():
    scraper.driver("socks", "inr")
    scraper.driver("socks", None, csv=True, cd=".")
    scraper.driver("socks", None, ui=True, csv=True, cd = ".")
    scraper.driver("socks", "USD", ui=True, sort="rades")
    scraper.driver("socks", None, ui=True, sort="raasc")
    scraper.driver("socks", None, ui=True, sort="pasc")
    scraper.driver("socks", None, ui=True, sort="asc")

def test_amazon_scraper():
    products = scraper.searchAmazon('table',False,None)
    price = scraper.amazon_scraper(products[0]['link'])

    assert price is None or type(price) == str

def test_walmart_scraper():
    products = scraper.searchWalmart('table',False,None)
    price = scraper.walmart_scraper(products[0]['link'])

    assert price is None or type(price) == str

def test_ebay_scraper():
    products = scraper.searchEbay('table',False,None)
    price = scraper.ebay_scraper(products[0]['link'])

    assert price is None or type(price) == str

def test_bestbuy_scraper():
    products = scraper.searchBestbuy('table',False,None)
    price = scraper.bestbuy_scraper(products[0]['link'])

    assert price is None or type(price) == str

def test_target_scraper():
    products = scraper.searchTarget('table',False,None)
    price = scraper.target_scraper(products[0]['link'])

    assert price is None or type(price) == str

def test_google_scraper():
    products = scraper.searchGoogleShopping('table',False,None)
    price = scraper.google_scraper(products[0]['link'])

    assert price is None or type(price) == str