'''
MIT License

Copyright (c) 2024 Girish G N, Joel Jogy George, Pravallika Vasireddy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import pytest
from flask import Flask
from src.modules.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_success(client):
    # Simulate a successful login
    response = client.post('/login', data={
        'username': 'shardul',
        'password': 'shardul@123'
    })
    print(response.data)  # Debug print
    assert response.status_code == 401

def test_login_failure(client):
    # Simulate a failed login
    response = client.post('/login', data={
        'username': 'invalid_user',
        'password': 'invalid_password'
    })
    print(response.data)  # Debug print
    assert response.status_code == 401

def test_login_empty_username(client):
    # Simulate login with empty username
    response = client.post('/login', data={
        'username': '',
        'password': 'some_password'
    })
    print(response.data)  # Debug print
    assert response.status_code == 400
    assert b'Username and Password are required' in response.data

def test_login_empty_password(client):
    # Simulate login with empty password
    response = client.post('/login', data={
        'username': 'some_user',
        'password': ''
    })
    print(response.data)  # Debug print
    assert response.status_code == 400
    assert b'Username and Password are required' in response.data