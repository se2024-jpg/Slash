import json
import os
import pandas as pd
import numpy as np
from pathlib import Path

# path for user profiles and their wish lists
users_main_dir = Path(__file__).parent.parent / "users"
users_main_dir.mkdir(parents=True, exist_ok=True)

def create_user(username):
    user_dir = users_main_dir / username
    if os.path.exists(user_dir): # user already exist
        return False
    else: # create new user
        user_dir.mkdir(parents=True, exist_ok=True)
        return True

def list_users():
    ls = os.listdir(users_main_dir)
    list_of_users = filter(lambda u: os.path.isdir(os.path.join(users_main_dir, u)), ls)
    return list_of_users