import json
import os
import pandas as pd
import numpy as np
from pathlib import Path
import re

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
                update_link(obj['link'],obj['website'],obj['price'])
            return csv
        except Exception:
            return pd.DataFrame()
    else:
        print("Doesnt exist")
        return None # wishlist not found

def wishlist_remove_list(username, wishlist_name, indx):
    wishlist_path = usr_dir(username) / (wishlist_name + ".csv")
    old_data = read_wishlist(username, wishlist_name)
    old_data = old_data.drop(index=indx)
    old_data.to_csv(wishlist_path, index=False, header=old_data.columns)

def find_currency(price):
    currency = re.match(r'^[a-zA-Z]{3,5}', price)
    return currency.group() if currency else currency
    pass

def update_link(link,website,price):
    currency = find_currency(price)
    if website == "amazon":
        pass
    if website == "Google":
        pass
    if website == "BJS":
        pass
    if website == "Etsy":
        pass
    if website == "walmart":
        pass