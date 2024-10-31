import pytest
import sys
from io import StringIO
from flask import session
from src.modules.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_landing_page(client):
    response = client.get('/')
    assert response.status_code == 200
#    assert b"Landing Page Content" in response.data  # Adjust based on actual landing page content


def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
#    assert b"Login Page Content" in response.data  # Adjust based on actual login page content
#

def test_register_page(client):
    response = client.get('/register')
    assert response.status_code == 200
#    assert b"Register Page Content" in response.data  # Adjust based on actual register page content


def test_google_login(client):
    response = client.get('/login/google')
    assert response.status_code == 302  # Redirect to Google OAuth

def test_logout(client):
    with client.session_transaction() as sess:
        sess['username'] = 'testuser'

    response = client.get('/logout')
    assert response.status_code == 200

def test_product_search(client, monkeypatch):
    def mock_driver(product, currency, num, min_price, max_price, min_rating, website, sort):
        return [{"title": "Product 1", "price": 100}]

    #monkeypatch.setattr("app.driver", mock_driver)

    response = client.get('/search', query_string={'product_name': 'test_product'})
    assert response.status_code == 200
    #assert b"Product 1" in response.data


def test_product_search_filtered(client, monkeypatch):
    def mock_product_search(*args, **kwargs):
        return [{"title": "Product 2", "price": 200}]

    #monkeypatch.setattr("app.product_search", mock_product_search)

    response = client.get('/filter', query_string={'product_name': 'filtered_product'})
    assert response.status_code == 200
    #assert b"Product 2" in response.data

def test_export_csv(client, monkeypatch):
    def mock_driver(*args, **kwargs):
        return [{"title": "Product 1", "link": "http://example.com/1", "rating": 4.5, "price": 100}]

    #monkeypatch.setattr("app.driver", mock_driver)

    response = client.get('/export_csv', query_string={'product_name': 'test_product'})
    assert response.status_code == 200
    assert response.headers["Content-type"] == "text/csv"
#    assert 'attachment; filename=test_product.csv' in response.headers['Content-Disposition']
#    assert b"Product 1" in response.data

                                        
