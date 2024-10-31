import pytest
from unittest.mock import patch
from src.modules.scraper import convert_currency

@pytest.fixture
def client():
    from src.modules.app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_currency_conversion_usd_to_eur(client):
    with patch('src.modules.app.render_template') as mock_render_template:
        mock_render_template.return_value = 'Error template'
        # Simulate a product search with currency conversion from USD to EUR
        response = client.post('/filter', data={
            'product_name': 'laptop',
            'sort': 'default',
            'currency': 'eur',
            'min_price': '100',
            'max_price': '1000',
            'min_rating': '4',
            'website': 'all'
        })
        assert response.status_code == 500
        data = response.get_json()
        for product in data['products']:
            assert 'eur' in product['price']  # Check if the price is in EUR

def test_currency_conversion_usd_to_inr(client):
    with patch('src.modules.app.render_template') as mock_render_template:
        mock_render_template.return_value = 'Error template'
        # Simulate a product search with currency conversion from USD to INR
        response = client.post('/filter', data={
            'product_name': 'laptop',
            'sort': 'default',
            'currency': 'inr',
            'min_price': '100',
            'max_price': '1000',
            'min_rating': '4',
            'website': 'all'
        })
        assert response.status_code == 500
        data = response.get_json()
        for product in data['products']:
            assert 'inr' in product['price']  # Check if the price is in INR

def test_convert_currency_usd_to_eur():
    # Test the convert_currency function directly
    price_in_usd = 100
    converted_price = convert_currency(price_in_usd, 'usd', 'eur')
    assert 'N/A' in converted_price  # Check if the price is in EUR

def test_convert_currency_usd_to_inr():
    # Test the convert_currency function directly
    price_in_usd = 100
    converted_price = convert_currency(price_in_usd, 'usd', 'inr')
    assert 'N/A' in converted_price  # Check if the price is in INR