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

    # Attempt to create the same user again
    assert not create_user(username, password)  # Should return False


