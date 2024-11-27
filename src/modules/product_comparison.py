"""
Copyright (C) 2024 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com
"""

"""
The scraper module holds functions that actually scrape the e-commerce websites
"""
from .scraper import searchAmazon, searchEbay, searchWalmart, searchBestbuy

def scrape_website(website, product, currency):
    # Normalize the website name for easier matching
    website = website.lower()
    p = []
    # Call the appropriate scraper function based on the website
    if website == 'walmart':
        p = searchWalmart(product, 0, currency)[0] #Need to include df_flag
    elif website == 'amazon':
        p = searchAmazon(product, 0, currency)[0] #Need to include df_flag
    elif website == 'ebay':
        p = searchEbay(product, 0, currency)[0] #Need to include df_flag
    elif website == 'bestbuy':
        p = searchBestbuy(product, 0, currency)[1] #Need to include df_flag
    # Add more elif clauses for other websites
    else:
        raise ValueError(f"Scraping for the website '{website}' is not supported.")
    
    # Fix URLs
    if "link" in p and "http" not in p["link"]:
        p["link"] = "http://" + p["link"]

    return p