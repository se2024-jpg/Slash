from genericpath import exists
import json
import os
import pandas as pd
from src.modules.scraper import driver
import webbrowser
import numpy as np
from pathlib import Path
from shutil import get_terminal_size

from src.modules.features import users_main_dir, create_user, list_users, create_wishlist, delete_wishlist, list_wishlists, read_wishlist, wishlist_add_item, wishlist_remove_list

class full_version:
    def __init__(self):
        self.name = "default"
        self.default_user_file = users_main_dir / "default_user.json"
        self.df = pd.DataFrame()
        self.currency = ""
        pd.set_option("display.max_rows", None)
        pd.set_option("display.max_columns", None)
        pd.set_option("display.width", get_terminal_size()[0])
        pd.set_option("display.max_colwidth", 40)

    def login(self):
        """Used for User Login
        Returns the username and email"""
        if not os.path.exists(self.default_user_file):
            print("Welcome to Slash!")
            print("Please enter the following information: ")
            name = input("Name: ")
            user_data = {"name": name}
            with open(self.default_user_file, "w") as outfile:
                json.dump(user_data, outfile)
            self.name = name
            create_user(self.name)

        else:
            with open(self.default_user_file) as json_file:
                data = json.load(json_file)
                self.name = data["name"]
        return self.name
    def search_fn(self):
        """Function searches for a given product and returns full list of products scraped.
        It then gives the user and option to save an item or open an item in browser"""
        prod = input("Enter name of product to Search: ")
        self.scrape(prod)
        ch = input(
            "\nEnter 1 to save product to wishlist \nEnter 2 to open link in browser\nElse enter any other key to continue\n"
        )
        try:
            ch = int(ch)
        except Exception:
            pass
        """By selecting 1, the User can store a searched product into a wishlist. Multiple wishlist are available and it has to be pre-selected 
        to store an item into it."""
        if ch == 1:
            wish_lists = self.wishlist_maker()
            wishlist_index = int(input("\nEnter your wishlist index: "))
            selected_wishlist = wish_lists[wishlist_index]
            """Select the row number of the product to save into the selected wishlist."""
            indx = int(input("\nEnter row number of product to save: "))
            if indx < len(self.df):
                new_data = self.df.iloc[[indx]]
                wishlist_add_item(self.name, selected_wishlist, new_data)
                """
                if os.path.exists(wishlist_path) and (
                    os.path.getsize(wishlist_path) > 0
                ):
                    old_data = pd.read_csv(wishlist_path)
                else:
                    old_data = pd.DataFrame()
                if self.df.title[indx] not in old_data:
                    final_data = pd.concat([old_data, new_data])
                    print("Item added successfully")
                final_data.to_csv(wishlist_path, index=False, header=self.df.columns)
                """
        """Selecting 2 allows the user to open the searched item in a broswer"""
        if ch == 2:
            indx = int(input("\nEnter row number of product to open: "))
            webbrowser.open_new(self.df.link[indx])

        return

    def extract_list(self):
        """This function helps user extract saved products, create new lists, modify list or open product in browser"""
        wish_lists = self.wishlist_maker()
        wishlist_options = int(
            input(
                "\nSelect from the following: \n1. Open Wishlist \n2. Create new Wishlist \n3. Delete Wishlist \n4. Return to Main\n"
            )
        )

        if wishlist_options == 1:
            wishlist_index = int(input("\nEnter the wishlist index: "))
            selected_wishlist = wish_lists[wishlist_index]
            items_data = read_wishlist(self.name, selected_wishlist)
            if items_data is not None:
                if(len(items_data)):
                    print(items_data)
                else:
                    print("Empty Wishlist")
                """
            wishlist_path = self.user_list_dir / selected_wishlist
            if os.path.exists(wishlist_path):
                try:
                    old_data = pd.read_csv(wishlist_path)
                    print(old_data)
                except Exception:
                    old_data = pd.DataFrame()
                    print("Empty Wishlist")
                """
                choice = int(
                    input(
                        "\nSelect from the following:\n1. Delete item from list\n2. Open link in Chrome\n3. Return to Main\n"
                    )
                )
                if choice == 1:
                    indx = int(input("\nEnter row number to be removed: "))
                    wishlist_remove_list(self.name, selected_wishlist, indx)
                if choice == 2:
                    indx = int(input("\nEnter row number to open in chrome: "))
                    url = items_data.link[indx]
                    webbrowser.open_new(url)
            else:
                print("Wishlist doesnot exist")

        elif wishlist_options == 2:
            wishlist_name = str(input("\nName your wishlist: "))
            create_wishlist(self.name, wishlist_name)

        elif wishlist_options == 3:
            wishlist_index = int(input("Enter the wishlist index to delete: "))
            selected_wishlist = wish_lists[wishlist_index]
            delete_wishlist(self.name, selected_wishlist)
        else:
            print("No saved data found.")

    def wishlist_maker(self):
        wish_lists = []
        print("----------Wishlists---------")
        for index, wishlist in enumerate(list_wishlists(self.name)):
            wish_lists.append(wishlist)
            print(index, "\t", wishlist)
        return wish_lists

    def view_users(self):
        users_list = []
        print("----------Users---------")
        for user in list_users():
            users_list.append(user)
            print("\t", user)
        return users_list

    def change_user(self):
        self.view_users()
        username = input("Enter username (username will be created if not exist):")
        create_user(username)
        self.name = username
        user_data = {"name": username}
        with open(self.default_user_file, "w") as outfile:
            json.dump(user_data, outfile)
        print("Welcome ", self.name)

    def scrape(self, prod):
        """calls the scraper function from scraper.py"""
        results = driver(prod, df_flag=1, currency=self.currency)
        # results = formatter.sortList(results, "ra" , True)
        self.df = pd.DataFrame.from_dict(results, orient="columns")
        print(self.df)
        #print(self.df.replace("", np.nan).dropna())

    def driver(self):
        self.login()
        flag_loop = 1
        print("Welcome ", self.name)
        while flag_loop == 1:
            print("Select from following:")
            print(
                "1. Search new product\n2. Manage Wishlists\n3. See Currency Conversion\n4. Change user\n0. Exit"
            )
            choice = int(input())
            if choice == 1:
                self.search_fn()
            elif choice == 2:
                self.extract_list()
            elif choice == 3:
                self.currency = str.lower(input("Enter INR/EUR\n"))
            elif choice == 4:
                self.change_user()
            elif choice == 0:
                print("Thank You for Using Slash")
                flag_loop = 0
            else:
                print("Incorrect Option")
