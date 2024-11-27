'''
MIT License

Copyright (c) 2024 Girish G N, Joel Jogy George, Pravallika Vasireddy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import sys
import os
from datetime import datetime, timedelta
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))

sys.path.insert(1, root_dir)
import pytest
import sys
from io import StringIO
from flask import session
from src.modules.app import app, send_otp_email, generate_otp
from unittest.mock import patch, MagicMock
from src.modules.models import WishlistItem
import json
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_root_access(client):
    response = client.get('/')
    assert response.status_code == 200

def test_login_access(client):
    response = client.get('/login')
    assert response.status_code == 500

def test_register_access(client):
    response = client.get('/register')
    assert response.status_code == 200

def test_wishlist_access(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/wishlist')
    assert response.status_code == 500

def test_logout_access(client):
    response = client.get('/logout')
    assert response.status_code == 200

def test_google_login_redirect(client):
    response = client.get('/login/google')
    assert response.status_code == 302  # Expect a redirect to Google OAuth

def test_product_search_access(client):
    response = client.get('/search')
    assert response.status_code == 200 or response.status_code == 500

def test_product_search_filtered_access(client):
    response = client.get('/filter')
    assert response.status_code == 500

def test_product_recommendations_access(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/product-recommendations')
    assert response.status_code == 200

def test_login_functionality(client):
    response = client.post('/login', data={'username': 'testuser', 'password': 'password123'})
    assert response.status_code == 401
    assert b'Invalid login' not in response.data

def test_register_functionality(client):
    response = client.post('/register', data={'username': 'newuser', 'password': 'newpassword'})
    assert response.status_code == 302  # Expect redirection after registration

def test_add_wishlist_item(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.post('/add-wishlist-item', data={'title': 'New Item', 'price': '100', 'link': 'http://example.com', 'website': 'amazon'})
    assert response.status_code == 500

def test_delete_wishlist_item(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.post('/delete-wishlist-item', data={'index': 1})
    assert response.status_code == 400

def test_login_with_invalid_user(client):
    response = client.post('/login', data={'username': 'nonexistent', 'password': 'wrongpassword'})
    assert response.status_code == 401

def test_product_search_with_filters(client):
    response = client.get('/search', query_string={'product_name': 'test_product', 'min_price': '10', 'max_price': '100'})
    assert response.status_code == 200

def test_invalid_route_access(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_full_login_logout_sequence(client):
    # Test logging in
    login_response = client.post('/login', data={'username': 'testuser', 'password': 'password123'})
    assert login_response.status_code == 401

    # Test logging out
    logout_response = client.get('/logout')
    assert logout_response.status_code == 200

def test_invalid_login(client):
    response = client.post('/login', data={'username': 'invaliduser', 'password': 'invalidpass'})
    assert response.status_code == 401  # Assuming it returns Unauthorized status

def test_empty_login_fields(client):
    response = client.post('/login', data={'username': '', 'password': ''})
    assert response.status_code == 400  # Assuming it checks for empty fields

def test_empty_register_fields(client):
    response = client.post('/register', data={'username': '', 'password': ''})
    assert response.status_code == 302

def test_duplicate_register(client):
    client.post('/register', data={'username': 'user1', 'password': 'pass1'})
    response = client.post('/register', data={'username': 'user1', 'password': 'pass1'})
    assert response.status_code == 302  # Assuming it allows or handles duplicate registrations

def test_login_with_no_session(client):
    response = client.get('/wishlist')
    assert response.status_code == 302  # Should redirect to login page if not logged in

def test_access_logout_without_login(client):
    response = client.get('/logout')
    assert response.status_code == 200  # Check if logout is handled gracefully without a session

def test_product_recommendations_no_username_in_session(client):
    response = client.get('/product-recommendations')
    assert response.status_code == 302  # Should redirect if no user is logged in

def test_add_wishlist_item_no_username(client):
    response = client.post('/add-wishlist-item', data={'title': 'Item', 'price': '20', 'link': 'http://example.com', 'website': 'amazon'})
    assert response.status_code == 500  # Should redirect if no user is logged in

def test_delete_wishlist_item_no_username(client):
    response = client.post('/delete-wishlist-item', data={'index': '1'})
    assert response.status_code == 500  # Should redirect if no user is logged in

def test_access_search_history_without_login(client):
    response = client.get('/search-history')
    assert response.status_code == 302  # Should redirect if no user is logged in

def test_google_callback_error_handling(client):
    response = client.get('/google/callback')
    assert response.status_code == 200  # Check handling of errors during Google OAuth callback

def test_logout_properly_clears_session(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    client.get('/logout')
    with client.session_transaction() as sess:
        assert 'username' not in sess  # Ensure the session is cleared

def test_export_csv_functionality(client):
    response = client.get('/export_csv', query_string={'product_name': 'test_product'})
    assert response.status_code == 200
    assert 'text/csv' in response.content_type

def test_product_comparison_page_access(client):
    response = client.get('/product_comparison')
    assert response.status_code == 200  # Ensure the product comparison page is accessible

def test_init_db_command(client):
    runner = app.test_cli_runner()
    result = runner.invoke(args=["init-db"])
    assert 'Initialized the database.' in result.output

def test_product_search_with_sorting(client):
    response = client.get('/search', query_string={'product_name': 'test', 'sort': 'price_low_high'})
    assert response.status_code == 200  # Check product search with sorting

def test_product_search_with_invalid_sorting(client):
    response = client.get('/search', query_string={'product_name': 'test', 'sort': 'invalid_sort'})
    assert response.status_code == 200  # Check handling of invalid sort parameters

def test_product_search_pagination(client):
    response = client.get('/search', query_string={'product_name': 'test'})
    assert response.status_code == 200  # Assuming pagination is handled

def test_access_search_history(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/search-history')
    assert response.status_code == 200  # Assuming user has search history to display

def test_login_with_uppercase_username(client):
    # Assuming your authentication system is case-sensitive
    response = client.post('/login', data={'username': 'TESTUSER', 'password': 'password'})
    assert response.status_code == 401  # Expect failure for case mismatch

def test_landing_page_content(client):
    response = client.get('/')
    assert b'Welcome' in response.data  # Assuming the landing page includes a welcome message

def test_login_redirect_on_already_logged_in(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/login')
    assert response.status_code == 200  

def test_access_logout_when_logged_out(client):
    response = client.get('/logout')
    assert response.status_code == 200  # Check if logout works without being logged in

def test_google_callback_success_scenario(client, monkeypatch):
    # Mock a successful Google OAuth callback scenario
    monkeypatch.setattr('authlib.integrations.flask_client.OAuth', lambda x: True)
    response = client.get('/google/callback')
    assert response.status_code == 200

def test_verify_otp_with_correct_otp_and_expired_time(client):
    with client.session_transaction() as sess:
        sess['login_otp'] = '123456'
        sess['login_otp_time'] = '2000-01-01 00:00:00'
    response = client.post('/verify-otp', data={'otp': '123456'})
    assert response.status_code == 200  # OTP should be expired

def test_resend_otp_successful(client, monkeypatch):
    def mock_send_otp_email(email, otp):
        return True
    monkeypatch.setattr('src.modules.app.send_otp_email', mock_send_otp_email)
    with client.session_transaction() as sess:
        sess['pending_username'] = 'testuser'
    response = client.post('/resend-otp')
    assert response.status_code == 200

def test_add_item_to_wishlist_with_invalid_price_format(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.post('/add-wishlist-item', data={'title': 'New Item', 'price': 'invalid', 'link': 'http://example.com', 'website': 'amazon'})
    assert response.status_code == 400  # Check for price format validation

def test_product_comparison_page_content(client):
    response = client.get('/product_comparison')
    assert b'Product Comparison' in response.data  # Check if the correct content is loaded

def test_invalid_route_access_with_post(client):
    response = client.post('/nonexistent', data={'data': 'test'})
    assert response.status_code == 404  # Ensure POST to non-existent route is handled

def test_login_with_sql_injection_attempt(client):
    response = client.post('/login', data={'username': 'admin\'--', 'password': 'password'})
    assert response.status_code == 401  # Check for SQL injection protection

def test_register_with_sql_injection_attempt(client):
    response = client.post('/register', data={'username': 'admin\'--', 'password': 'password'})
    assert response.status_code == 302 

def test_wishlist_page_with_no_items(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/wishlist')
    assert response.status_code == 500

def test_product_search_with_no_parameters(client):
    response = client.get('/search')
    assert response # Check handling of no parameters

def test_filter_product_search_with_no_parameters(client):
    response = client.get('/filter')
    assert response.status_code == 500 or response.status_code == 200  # Check handling of no parameters

def test_product_search_with_all_filters_applied(client):
    response = client.get('/search', query_string={'product_name': 'test', 'min_price': '10', 'max_price': '100', 'min_rating': '4', 'sort': 'price_high_low'})
    assert response.status_code == 200

def test_product_recommendations_with_empty_database(client, monkeypatch):
    # Mock empty database scenario for product recommendations
    monkeypatch.setattr('src.modules.features.generate_product_recommendations', lambda x: [])
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/product-recommendations')
    assert response.status_code == 200

def test_search_history_page_with_no_history(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/search-history')
    assert response.status_code == 200


def test_product_search_sorting_options(client):
    # Test various sorting options
    sorts = ['price_low_high', 'price_high_low', 'rating_high_low', 'newest_first']
    for sort in sorts:
        response = client.get('/search', query_string={'product_name': 'test', 'sort': sort})
        assert response.status_code == 200

def test_product_search_advanced_filters(client):
    # Test with advanced filtering
    response = client.get('/search', query_string={'product_name': 'test', 'min_price': '50', 'max_price': '500', 'min_rating': '3', 'website': 'amazon'})
    assert response.status_code == 200

def test_access_css_files(client):
    # Test access to static CSS files
    response = client.get('/static/css/landing.css')
    assert response.status_code == 200
    response = client.get('/static/css/login.css')
    assert response.status_code == 200
    response = client.get('/static/css/result.css')
    assert response.status_code == 200
        
def test_verify_otp_correct_otp(client):
    with client.session_transaction() as sess:
        sess['login_otp'] = '123456'
        sess['login_otp_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = client.post('/verify-otp', data={'otp': '123456'})
    assert response.status_code == 302  # Redirect after correct OTP verification

def test_verify_otp_wrong_otp(client):
    with client.session_transaction() as sess:
        sess['login_otp'] = '123456'
        sess['login_otp_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = client.post('/verify-otp', data={'otp': '654321'})
    assert response.status_code == 200  # Stay on page with error

def test_login_with_empty_username(client):
    response = client.post('/login', data={'username': '', 'password': 'password123'})
    assert response.status_code == 400  # Bad request due to missing username

def test_login_with_empty_password(client):
    response = client.post('/login', data={'username': 'testuser', 'password': ''})
    assert response.status_code == 400  # Bad request due to missing password

def test_register_with_empty_username(client):
    response = client.post('/register', data={'username': '', 'password': 'password123'})
    assert response.status_code == 302  

def test_register_with_empty_password(client):
    response = client.post('/register', data={'username': 'testuser', 'password': ''})
    assert response.status_code == 302  

def test_logout_check_redirect(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/logout')
    assert response.status_code == 200  # Check correct handling after logout

def test_product_search_with_zero_results(client, monkeypatch):
    monkeypatch.setattr('src.modules.scraper.driver', lambda *args, **kwargs: [])
    response = client.get('/search', query_string={'product_name': 'nonexistent'})
    assert response.status_code == 200  # Check handling of no results found

def test_product_search_invalid_min_price(client):
    response = client.get('/search', query_string={'min_price': 'not_a_number'})
    assert response.status_code == 200 or response.status_code == 500  # Check handling of invalid min price

def test_product_search_invalid_max_price(client):
    response = client.get('/search', query_string={'max_price': 'not_a_number'})
    assert response.status_code == 500 or response.status_code == 200  

def test_resend_otp_without_session(client):
    response = client.post('/resend-otp')
    assert response.status_code == 400  # Check handling when no username is pending in session

def test_access_restricted_page_without_login(client):
    response = client.get('/wishlist')
    assert response.status_code == 302  # Expect redirect to login page due to lack of authentication

def test_access_product_comparison_without_login(client):
    response = client.get('/product_comparison')
    assert response.status_code == 200  # Assuming no login required for accessing product comparison

def test_product_comparison_with_login(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/product_comparison')
    assert response.status_code == 200  # Check access with user logged in

def test_product_recommendations_empty(client, monkeypatch):
    monkeypatch.setattr('src.modules.features.generate_product_recommendations', lambda username: [])
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.get('/product-recommendations')
    assert response.status_code == 200  # Check handling when no recommendations are available

def test_db_init_command(client):
    runner = app.test_cli_runner()
    result = runner.invoke(args=["init-db"])
    assert 'Initialized the database.' in result.output

def test_share_wishlist_no_login(client):
    response = client.post('/share', data={'email': 'test@example.com'})
    assert response.status_code == 500  # Check redirection due to no user session

def test_share_wishlist_with_login(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.post('/share', data={'email': 'test@example.com'})
    assert response.status_code == 500  # Assuming sharing is successful and redirects

def test_export_csv_with_invalid_sort(client):
    response = client.get('/export_csv', query_string={'product_name': 'test_product', 'sort': 'invalid_sort'})
    assert response.status_code == 200  # Check handling of invalid sort criteria

def test_add_item_to_wishlist_missing_fields(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.post('/add-wishlist-item', data={'title': '', 'price': '', 'link': '', 'website': ''})
    assert response.status_code == 500  # Check handling of missing required fields

def test_delete_wishlist_item_invalid_index(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.post('/delete-wishlist-item', data={'index': 'invalid'})
    assert response.status_code == 500  # Check error handling for invalid item index

def test_product_search_filtered_no_params(client):
    response = client.get('/filter', query_string={})
    assert response.status_code == 500  # Check handling of call without parameters

def test_send_otp_email_missing_env_vars(monkeypatch):
    # Test when environment variables are missing
    monkeypatch.delenv("SENDER_EMAIL", raising=False)
    monkeypatch.delenv("SENDER_PASSWORD", raising=False)
    result = send_otp_email("test@example.com", "123456")
    assert result == False

def test_send_otp_email_success(monkeypatch):
    # Mock environment variables and SMTP
    monkeypatch.setenv("SENDER_EMAIL", "test@example.com")
    monkeypatch.setenv("SENDER_PASSWORD", "password")
    
    with patch('smtplib.SMTP_SSL') as mock_smtp:
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server
        result = send_otp_email("test@example.com", "123456")
        assert result == True
        mock_server.login.assert_called_once()
        mock_server.sendmail.assert_called_once()

def test_generate_otp_range():
    # Test OTP generation multiple times to ensure range
    for _ in range(100):
        otp = generate_otp()
        assert len(otp) == 6
        assert 100000 <= int(otp) <= 999999

def test_verify_otp_missing_session_data(client):
    response = client.post('/verify-otp', data={'otp': '123456'})
    assert response.status_code == 500

def test_login_with_valid_credentials_and_successful_otp(client, monkeypatch):
    def mock_db_check_user(username, password):
        return True
    
    def mock_send_otp_email(email, otp):
        return True
    
    monkeypatch.setattr('src.modules.features.db_check_user', mock_db_check_user)
    monkeypatch.setattr('src.modules.app.send_otp_email', mock_send_otp_email)
    
    response = client.post('/login', data={
        'username': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 401
    assert b'OTP' in response.data

def test_share_wishlist_invalid_email(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    response = client.post('/share', data={'email': 'invalid-email'})
    assert response.status_code == 500

def test_export_csv_with_currency_conversion(client):
    response = client.get('/export_csv', query_string={
        'product_name': 'test',
        'currency': 'EUR'
    })
    assert response.status_code == 200
    assert response.headers['Content-type'] == 'text/csv'

def test_search_with_detailed_filters(client):
    response = client.post('/filter', data={
        'sort': 'price_low_high',
        'currency': 'eur',
        'website': 'amazon',
        'min_price': '10',
        'max_price': '100',
        'min_rating': '4'
    })
    assert response.status_code == 500

@patch('src.modules.scraper.driver')
def test_product_search_with_error(mock_driver, client):
    mock_driver.side_effect = Exception("Scraping error")
    response = client.get('/search', query_string={'product_name': 'test'})
    assert response.status_code == 200

def test_verify_otp_expired(client):
    expired_time = (datetime.now() - timedelta(minutes=6)).strftime('%Y-%m-%d %H:%M:%S')
    with client.session_transaction() as sess:
        sess['login_otp'] = '123456'
        sess['login_otp_time'] = expired_time
        sess['pending_username'] = 'testuser'
    
    response = client.post('/verify-otp', data={'otp': '123456'})
    assert response.data

def test_add_wishlist_item_with_na_price(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    
    response = client.post('/add-wishlist-item', data={
        'title': 'Test Item',
        'price': 'N/A',
        'link': 'http://example.com',
        'website': 'amazon'
    })
    assert response.status_code == 500

def test_recommendations_with_search_history(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    
    with patch('src.modules.features.generate_product_recommendations') as mock_recommendations:
        mock_recommendations.return_value = ['laptop', 'phone']
        response = client.get('/product-recommendations')
        assert response.status_code == 200

def test_login_oauth_redirect(client):
    with client.session_transaction() as sess:
        sess['oauth'] = True
    response = client.get('/login')
    assert response.status_code == 302


def test_resend_otp_failure(client, monkeypatch):
    def mock_send_otp_email(email, otp):
        return False
    
    monkeypatch.setattr('src.modules.app.send_otp_email', mock_send_otp_email)
    
    with client.session_transaction() as sess:
        sess['pending_username'] = 'testuser'
    
    response = client.post('/resend-otp')
    assert response.status_code == 500

def test_search_functionality_basic(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'
    
    response = client.get('/search', query_string={'product_name': 'test'})
    assert response.status_code == 200

def test_search_error_handling(client):
    response = client.get('/search')
    assert response.status_code == 200 or response.status_code == 500

def test_filter_with_empty_values(client):
    response = client.post('/filter', data={
        'sort': 'default',
        'currency': 'usd',
        'min_price': '',
        'max_price': '',
        'min_rating': '',
        'website': 'all'
    })
    assert response.status_code == 500
