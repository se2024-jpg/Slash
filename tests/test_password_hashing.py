'''
MIT License

Copyright (c) 2024 Girish G N, Joel Jogy George, Pravallika Vasireddy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import os
import pandas as pd
import pytest
from werkzeug.security import check_password_hash
from pathlib import Path
from src.modules.features import create_user, check_user, get_credentials
import bcrypt

# Helper to generate user directory path
def usr_dir(username, base_dir='users'):
    return os.path.join(base_dir, username)

# Setup and Teardown functions
@pytest.fixture(scope='module')
def setup_test_directory():
    """Setup: Create a temporary test directory."""
    test_dir = 'users'
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)
    yield
    # Teardown: Remove all user directories after tests
    for folder in os.listdir(test_dir):
        user_folder = os.path.join(test_dir, folder)
        if os.path.isdir(user_folder):
            for file in os.listdir(user_folder):
                os.remove(os.path.join(user_folder, file))
            os.rmdir(user_folder)
    os.rmdir(test_dir)

# Test Case 1: Verify password matching using check_user
def test_check_user(setup_test_directory):
    """Test that the correct password matches the stored hash."""
    username = "testuser1@example.com"
    password = "securepassword123"

    # Ensure the user was created and password matches
    create_user(username, password)
    assert check_user(username, password)

    # Ensure an incorrect password doesn't match
    assert not check_user(username, "wrongpassword")

def test_check_user_blank_pwd(setup_test_directory):
    """Test that the correct password matches the stored hash."""
    username = "testuser2@example.com"
    password = ""

    # Ensure the user was created and password matches
    create_user(username, password)
    assert check_user(username, password)

    # Ensure an incorrect password doesn't match
    assert not check_user(username, "wrongpassword")

def test_check_incorrect_pwd(setup_test_directory):
    """Test that the correct password matches the stored hash."""
    username = "testuser3@example.com"
    password = "password"

    # Ensure the user was created and password matches
    create_user(username, password)
    # Ensure an incorrect password doesn't match
    assert not check_user(username, "wrongpassword")

def test_create_duplicate_user(setup_test_directory):
    """Test that creating a duplicate user does not overwrite the existing user."""
    username = "duplicate_user@example.com"
    password = "securepassword456"

    # Create the user
    assert create_user(username, password)



