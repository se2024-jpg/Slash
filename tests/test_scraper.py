from src.modules import scraper

def test_filter():
    data = [ {"price": "$10", "rating": "4.5"}, {"price": "$20", "rating": "4.0"}, {"price": "$30", "rating": "3.5"}, {"price": "$40", "rating": "5"} ]
    result = scraper.filter(data, 25, None, None)
    assert len(result) == 2
    result = scraper.filter(data, None, 35, None)
    assert len(result) == 3
    result = scraper.filter(data, None, None, 4.1)
    assert len(result) == 2

def test_driver():
    scraper.driver("socks", "inr")
    #scraper.driver("socks", None, csv=True, cd='.')
    #scraper.driver("socks", None, ui=True, csv=True)
    scraper.driver("socks", None, ui=True, sort="rades")
    scraper.driver("socks", None, ui=True, sort="raasc")
    scraper.driver("socks", None, ui=True, sort="pasc")
    scraper.driver("socks", None, ui=True, sort="asc")
