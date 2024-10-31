"""
Copyright (C) 2023 SE23-Team44
 
Licensed under the MIT License.
See the LICENSE file in the project root for the full license information.
"""

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

    if products:
        price = scraper.amazon_scraper(products[0]['link'])
        assert price is None or type(price) == str

def test_walmart_scraper():
    products = scraper.searchWalmart('table',False,None)
    
    if products:
        price = scraper.walmart_scraper(products[0]['link'])
        assert price is None or type(price) == str

def test_ebay_scraper():
    products = scraper.searchEbay('table',False,None)

    if products:
        price = scraper.ebay_scraper(products[0]['link'])
        assert price is None or type(price) == str

def test_bestbuy_scraper():
    products = scraper.searchBestbuy('table',False,None)

    if products:
        price = scraper.bestbuy_scraper(products[0]['link'])
        assert price is None or type(price) == str

# def test_target_scraper(): No longer used
#     products = scraper.searchTarget('table',False,None)
    
#     if products:
#         price = scraper.target_scraper(products[0]['link'])
#         assert price is None or type(price) == str

def test_google_scraper():
    products = scraper.searchGoogleShopping('table',False,None)

    if products:
        price = scraper.google_scraper(products[0]['link'])
        assert price is None or type(price) == str

def test_convert_currency_with_rate():
    # Simulate getting an exchange rate for USD to EUR
    rate_eur = 0.85  # For example, this might return 0.85
    rate_gbp = 0.75
    rate_usd = 1
    rate_inr = 84.09
    rate_yn = 7.12
    # Test with a valid amount and the retrieved rate
    amount = "$100.00"
    converted = scraper.convert_currency(amount, "EUR", rate_eur)
    assert converted == "EUR 85.00", f"Expected 'EUR 85.00', but got '{converted}'"

    # Test with another amount and a different rate
    amount = "$250.50"
    converted = scraper.convert_currency(amount, "GBP", rate_gbp)
    assert converted == "GBP 187.88", f"Expected 'GBP 187.88', but got '{converted}'"

    # Test with another amount and a different rate
    amount = "$250.50"
    converted = scraper.convert_currency(amount, "USD", rate_usd)
    assert converted == "USD 250.50", f"Expected 'USD 250.50', but got '{converted}'"

    # Test with another amount and a different rate
    amount = "$250.50"
    converted = scraper.convert_currency(amount, "INR", rate_inr)
    assert converted == "INR 21064.55", f"Expected 'INR 21064.55', but got '{converted}'"

    # Test with an amount without a currency symbol
    amount = "50"
    converted = scraper.convert_currency(amount, "CNY", rate_yn)
    assert converted == "CNY 356.00", f"Expected 'CNY 356.00', but got '{converted}'"

    # Test with a malformed amount (should raise ValueError)
    try:
        scraper.convert_currency("$abc", "EUR", rate_eur)
        assert False, "Expected Exception was not raised"
    except Exception:
        pass  # The ValueError is expected
