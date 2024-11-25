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
        # Simulating the product search result with currency conversion from USD to EUR
        mock_render_template.return_value = 'Error template'
        with patch('src.modules.scraper.convert_currency') as mock_convert_currency:
            mock_convert_currency.return_value = "85.00 EUR"  # Mocking the conversion result
            response = client.post('/filter', data={
                'product_name': 'laptop',
                'sort': 'default',
                'currency': 'eur',
                'min_price': '100',
                'max_price': '1000',
                'min_rating': '4',
                'website': 'all'
            })
            assert response.status_code == 200  # Simulating a successful response code
            data = response.get_json()
            for product in data['products']:
                assert 'eur' in product['price']  # Check if the price is in EUR

def test_currency_conversion_usd_to_inr(client):
    with patch('src.modules.app.render_template') as mock_render_template:
        # Simulating the product search result with currency conversion from USD to INR
        mock_render_template.return_value = 'Error template'
        with patch('src.modules.scraper.convert_currency') as mock_convert_currency:
            mock_convert_currency.return_value = "7500.00 INR"  # Mocking the conversion result
            response = client.post('/filter', data={
                'product_name': 'laptop',
                'sort': 'default',
                'currency': 'inr',
                'min_price': '100',
                'max_price': '1000',
                'min_rating': '4',
                'website': 'all'
            })
            assert response.status_code == 200  # Simulating a successful response code
            data = response.get_json()
            for product in data['products']:
                assert 'inr' in product['price']  # Check if the price is in INR

def test_convert_currency_usd_to_eur():
    price_in_usd = 100
    with patch('src.modules.scraper.convert_currency') as mock_convert_currency:
        mock_convert_currency.return_value = "85.00 EUR"  
        converted_price = convert_currency(price_in_usd, 'usd', 'eur')
        assert converted_price == "85.00 EUR"  # Ensure the mocked conversion value is returned

def test_convert_currency_usd_to_inr():
    price_in_usd = 100
    with patch('src.modules.scraper.convert_currency') as mock_convert_currency:
        mock_convert_currency.return_value = "7500.00 INR"  
        converted_price = convert_currency(price_in_usd, 'usd', 'inr')
        assert converted_price == "7500.00 INR"  
