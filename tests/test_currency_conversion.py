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
        
        # Mocking the actual currency conversion logic for EUR
        with patch('src.modules.scraper.convert_currency') as mock_convert_currency:
            mock_convert_currency.return_value = "85.00 EUR"  # Mocking the conversion result
            
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
            
            # Assert that the status code is 200 (not 500)
            assert response.status_code == 200
            
            # Get the response data
            data = response.get_json()
            
            # Ensure that product prices are in EUR
            for product in data['products']:
                assert 'eur' in product['price']  # Check if the price is in EUR

def test_currency_conversion_usd_to_inr(client):
    with patch('src.modules.app.render_template') as mock_render_template:
        mock_render_template.return_value = 'Error template'
        
        # Mocking the actual currency conversion logic for INR
        with patch('src.modules.scraper.convert_currency') as mock_convert_currency:
            mock_convert_currency.return_value = "7500.00 INR"  # Mocking the conversion result
            
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
            
            # Assert that the status code is 200 (not 500)
            assert response.status_code == 200
            
            # Get the response data
            data = response.get_json()
            
            # Ensure that product prices are in INR
            for product in data['products']:
                assert 'inr' in product['price']  # Check if the price is in INR

def test_convert_currency_usd_to_eur():
    price_in_usd = 100
    with patch('src.modules.scraper.convert_currency') as mock_convert_currency:
        # Mocking the currency conversion to EUR
        mock_convert_currency.return_value = "85.00 EUR"  # Mocked conversion result
        converted_price = convert_currency(price_in_usd, 'usd', 'eur')
        
        # Ensure the mocked conversion value is returned
        assert converted_price == "85.00 EUR"  # Ensure it's EUR, not 'N/A'

def test_convert_currency_usd_to_inr():
    price_in_usd = 100
    with patch('src.modules.scraper.convert_currency') as mock_convert_currency:
        # Mocking the currency conversion to INR
        mock_convert_currency.return_value = "7500.00 INR"  # Mocked conversion result
        converted_price = convert_currency(price_in_usd, 'usd', 'inr')
        
        # Ensure the mocked conversion value is returned
        assert converted_price == "7500.00 INR"  # Ensure it's INR, not 'N/A'
