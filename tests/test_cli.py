from src.modules import full_version
import random
import string
import os
import json

def test_set_player_name(monkeypatch):
    fv = full_version.full_version()
    if not os.path.exists(fv.user_data):
        name = "".join(random.choices(string.ascii_lowercase, k=5))
        email = "".join(random.choices(string.ascii_lowercase, k=3)) + "@mail.com"
        
        answers = iter([name, email])

        monkeypatch.setattr('builtins.input', lambda name: next(answers))

        assert fv.login() == (name, email)
    else:
        with open(fv.user_data) as json_file:
            data = json.load(json_file)
            name = data["name"]
            email = data["email"]
        assert fv.login() == (name, email)

def test_search_fn(monkeypatch):
    answers = iter([1, 3])