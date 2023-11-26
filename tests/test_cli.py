"""
Copyright (C) 2023 SE23-Team44
 
Licensed under the MIT License.
See the LICENSE file in the project root for the full license information.
"""

import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))

sys.path.insert(1, root_dir)
from src.modules import full_version
from src.modules import csv_writer
from src.modules import features
import random
import string
import os
import json
import pytest

def test_set_player_name(monkeypatch):
    fv = full_version.full_version()
    if not os.path.exists(fv.default_user_file):
        name = "".join(random.choices(string.ascii_lowercase, k=5))
        #email = "".join(random.choices(string.ascii_lowercase, k=3)) + "@mail.com"
        
        answers = iter([name])

        monkeypatch.setattr('builtins.input', lambda name: next(answers))

        assert fv.login() == name
    else:
        with open(fv.default_user_file) as json_file:
            data = json.load(json_file)
            name = data["name"]
            # email = data["email"]
        assert fv.login() == name

def test_change_user(monkeypatch, capfd):
    fv = full_version.full_version()
    features.create_user('test')
    fv.name = 'test'
    answers = iter(["user1"])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    fv.change_user()
    out, err = capfd.readouterr()
    assert "Welcome" in out

def test_extract_list(monkeypatch, capfd):
    fv = full_version.full_version()
    features.create_user('test')
    fv.name = 'test'
    wishlist_index = 0
    # Create a new wishlist
    answers = iter([2, wishlist_index, 3])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    fv.extract_list()
    out, err = capfd.readouterr()
    assert "Wishlists" in out

    # Adds an item to wish list
    answers = iter(["socks", 1, wishlist_index, 5])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    fv.search_fn()
    out, err = capfd.readouterr()
    assert "Item added successfully" in out

    answers = iter([1, wishlist_index, 3])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    fv.extract_list()
    out, err = capfd.readouterr()
    assert "Wishlists" in out

    # First "3" indicates deleting the index
    # Second "3" indicates closing the menu
    # Deletes the 0th index
    answers = iter([3, wishlist_index, 3])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    fv.extract_list()

    with pytest.raises(IndexError):
        answers = iter([1, 33, 3])
        monkeypatch.setattr('builtins.input', lambda name: next(answers))
        fv.extract_list()

def test_csv_writer():
    x = csv_writer.write_csv([{"name": "parth", "surname": "parikh", "age": 10}], "Names", ".")
    assert x[:5] == "Names"