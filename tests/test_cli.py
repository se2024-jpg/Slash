'''
MIT License

Copyright (c) 2024 Girish G N, Joel Jogy George, Pravallika Vasireddy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

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
        answers = iter([name])
        monkeypatch.setattr('builtins.input', lambda name: next(answers))

        assert fv.login() == name
    else:
        with open(fv.default_user_file) as json_file:
            data = json.load(json_file)
            name = data["name"]
        assert fv.login() == name

def test_change_user(monkeypatch, capfd):
    fv = full_version.full_version()
    features.create_user('test','pass')
    fv.name = 'test'
    answers = iter(["user1"])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    fv.change_user()
    out, err = capfd.readouterr()
    assert "Welcome" in out

def test_csv_writer():
    x = csv_writer.write_csv([{"name": "parth", "surname": "parikh", "age": 10}], "Names", ".")
    assert x[:5] == "Names"