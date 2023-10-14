import json
import os
import pandas as pd
import numpy as np
from pathlib import Path

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
    wishlist_filename = usr_dir(username) / (wishlist_name + ".csv")
    open(wishlist_filename, "a").close()

def list_wishlists(username):
    user_dir = usr_dir(username)
    wishlists = list(map(lambda w: w.replace(".csv", ""), os.listdir(user_dir)))
    return wishlists

def delete_wishlist(username, wishlist_name):
    wishlist_filename = usr_dir(username) / wishlist_name
    wishlist_filename.unlink(missing_ok=True)
