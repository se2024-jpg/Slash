import logging
from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse

def get_base_domain(url):
    """Extract the base domain from a URL"""
    parsed = urlparse(url)
    return parsed.netloc.lower()

def clean_price(price_str):
    """
    Clean and standardize price strings
    Returns: Price as float or None if invalid
    """
    if not price_str:
        return None
        
    # Extract price using regex - get just the number
    price_match = re.search(r'\$?\s*(\d+(?:,\d{3})*(?:\.\d{2})?)', price_str)
    if not price_match:
        return None
        
    # Clean and format price
    price = price_match.group(1).replace(',', '')
    try:
        return float(price)  # Return as float instead of formatted string
    except ValueError:
        return None

def create_session():
    """Create a session with proper headers for scraping"""
    session = requests.Session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    return session

def amazon_scraper(url, session):
    """Scrape price from Amazon product page"""
    try:
        response = session.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try multiple price selectors
        price_element = (
            soup.select_one('.a-price .a-offscreen') or
            soup.select_one('#priceblock_ourprice') or
            soup.select_one('#priceblock_saleprice') or
            soup.select_one('.a-price-whole')
        )
        

        if price_element:
            return clean_price(price_element.text)
        return None
            
    except Exception as e:
        logging.error(f"Error scraping Amazon price: {str(e)}")
        return None

def walmart_scraper(url, session):
    """Scrape price from Walmart product page"""
    try:
        response = session.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Try multiple price selectors
        price_element = (
            soup.find('span', itemprop='price') or
            soup.select_one('[itemprop="price"]') or
            soup.select_one('.price-characteristic') or
            soup.select_one('.price .visuallyhidden')
        )
        if price_element:
            return clean_price(price_element.text)
        return None
            
    except Exception as e:
        logging.error(f"Error scraping Walmart price: {str(e)}")
        return None

def ebay_scraper(url, session):
    """Scrape price from eBay product page"""
    try:
        response = session.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try multiple price selectors
        price_element = (
            soup.select_one('#prcIsum') or
            soup.select_one('#mm-saleDscPrc') or
            soup.select_one('.x-price-primary')
        )
        
        if price_element:
            return clean_price(price_element.text)
        return None
            
    except Exception as e:
        logging.error(f"Error scraping eBay price: {str(e)}")
        return None

def bestbuy_scraper(url, session):
    """Scrape price from Best Buy product page"""
    try:
        response = session.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try multiple price selectors
        price_element = (
            soup.select_one('.priceView-customer-price span') or
            soup.select_one('.priceView-hero-price span') or
            soup.select_one('[data-testid="customer-price"]')
        )
        
        if price_element:
            return clean_price(price_element.text)
        return None
            
    except Exception as e:
        logging.error(f"Error scraping Best Buy price: {str(e)}")
        return None

def scrape_price(url, store=None):
    """
    Main function to scrape price from a product URL
    Parameters:
        url: Product page URL
        store: Optional store identifier. If None, determined from URL
    Returns:
        Price as float or None if price couldn't be scraped
    """
    if not url:
        return None
        
    # Create session for scraping
    session = create_session()
    
    # Determine store from URL if not provided
    if not store:
        domain = get_base_domain(url)
        if 'amazon' in domain:
            store = 'amazon'
        elif 'walmart' in domain:
            store = 'walmart'
        elif 'ebay' in domain:
            store = 'ebay'
        elif 'bestbuy' in domain:
            store = 'bestbuy'
        else:
            logging.error(f"Unsupported store domain: {domain}")
            return None
            
    # Call appropriate scraper
    scrapers = {
        'amazon': amazon_scraper,
        'walmart': walmart_scraper,
        'ebay': ebay_scraper,
        'bestbuy': bestbuy_scraper
    }
    
    scraper_func = scrapers.get(store.lower())
    if not scraper_func:
        logging.error(f"No scraper implemented for store: {store}")
        return None
        
    price = scraper_func(url, session)
    
    return price  # Returns float value without currency symbol