import json
import os
import pandas as pd
import numpy as np
import re
import ssl
import smtplib
from pathlib import Path

from . import scraper
from email.message import EmailMessage


# path for user profiles and their wish lists
users_main_dir = Path(__file__).parent.parent / "users"
users_main_dir.mkdir(parents=True, exist_ok=True)

def usr_dir(username):
    return users_main_dir / username

def create_user(username):
    user_dir = usr_dir(username)
    if os.path.exists(user_dir): # user already exist
        return False
    else: # create new user
        user_dir.mkdir(parents=True, exist_ok=True)
        create_wishlist(username, 'default')
        return True

def list_users():
    ls = os.listdir(users_main_dir)
    list_of_users = list(filter(lambda u: os.path.isdir(os.path.join(users_main_dir, u)), ls))
    return list_of_users

def create_wishlist(username, wishlist_name):
    wishlist_path = usr_dir(username) / (wishlist_name + ".csv")
    open(wishlist_path, "a").close()

def list_wishlists(username):
    user_dir = usr_dir(username)
    wishlists = list(map(lambda w: w.replace(".csv", ""), os.listdir(user_dir)))
    return wishlists

def delete_wishlist(username, wishlist_name):
    wishlist_path = usr_dir(username) / (wishlist_name + ".csv")
    wishlist_path.unlink(missing_ok=True)

def wishlist_add_item(username, wishlist_name, item_data):
    if isinstance(item_data, dict):
        item_data = pd.DataFrame([item_data])
    wishlist_path = usr_dir(username) / (wishlist_name + ".csv")
    if os.path.exists(wishlist_path) and (os.path.getsize(wishlist_path) > 0 ):
        old_data = pd.read_csv(wishlist_path)
    else:
        old_data = pd.DataFrame()
    #if self.df.title[indx] not in old_data:
    final_data = pd.concat([old_data, item_data])
    final_data.to_csv(wishlist_path, index=False, header=item_data.columns)

def read_wishlist(username, wishlist_name):
    wishlist_path = usr_dir(username) / (wishlist_name + ".csv")
    if os.path.exists(wishlist_path):
        try:
            csv = pd.read_csv(wishlist_path)
            for _,obj in csv.iterrows():
                new_price = update_price(obj['link'],obj['website'],obj['price'])
                obj['price'] = new_price
            return csv
        except Exception:
            return pd.DataFrame()
    else:
        return None # wishlist not found

def share_wishlist(username, wishlist_name, email_receiver):
    wishlist_path = usr_dir(username) / (wishlist_name + ".csv")
    if os.path.exists(wishlist_path):
        try:
            email_sender = 'slash.se23@gmail.com'
            email_password = 'amkx fedi ilnm qahn'

            subject = ' slash wishlist of ' + username

            df = pd.read_csv(wishlist_path)
            body = df['link'].astype(str).str.cat(sep=' ')
            # body = df['link'].to_string(index=False)
            # body = df.to_string(index=False)

            em = EmailMessage()
            em['from'] = email_sender
            em['to'] = email_receiver
            em['subject'] = subject
            em.set_content(body)
            

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

        except Exception:
            return 'failed to send email'
    else:
        return None # wishlist not found

def wishlist_remove_list(username, wishlist_name, indx):
    wishlist_path = usr_dir(username) / (wishlist_name + ".csv")
    old_data = read_wishlist(username, wishlist_name)
    old_data = old_data.drop(index=indx)
    old_data.to_csv(wishlist_path, index=False, header=old_data.columns)

def find_currency(price):
    currency = re.match(r'^[a-zA-Z]{3,5}', price)
    return currency.group() if currency else currency

def update_price(link,website,price):
    currency = find_currency(price)
    updated_price = price
    if website == "amazon":
        scraped_price = scraper.amazon_scraper(link).strip()
        if scraped_price:
            updated_price = scraper.getCurrency(currency,scraped_price) if currency is not None else scraped_price
    if website == "google":
        scraped_price = scraper.google_scraper(link).strip()
        if scraped_price:
            updated_price = scraper.getCurrency(currency,scraped_price) if currency is not None else scraped_price
    if website == "BJS":
        pass
    if website == "Etsy":
        pass
    if website == "walmart":
        scraped_price = scraper.walmart_scraper(link).strip()
        if scraped_price:
            updated_price = scraper.getCurrency(currency,scraped_price) if currency is not None else scraped_price
    if website == "ebay":
        scraped_price = scraper.ebay_scraper(link).strip()
        if scraped_price:
            updated_price = scraper.getCurrency(currency,scraped_price) if currency is not None else scraped_price
    if website == "bestbuy":
        scraped_price = scraper.bestbuy_scraper(link).strip()
        if scraped_price:
            updated_price = scraper.getCurrency(currency,scraped_price) if currency is not None else scraped_price       
    if website == "target":
        scraped_price = scraper.target_scraper(link).strip()
        if scraped_price:
            updated_price = scraper.getCurrency(currency,scraped_price) if currency is not None else scraped_price      
    return updated_price
