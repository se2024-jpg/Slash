'''
MIT License

Copyright (c) 2024 Girish G N, Joel Jogy George, Pravallika Vasireddy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from src.modules import formatter
import math


def test_getNumbers():
    """
    Checks the getNumbers function
    """
    assert formatter.getNumbers("some chars and $10.00") == 10.0
    assert formatter.getNumbers("some chars and $10.99 some other chars") == 10.99

def test_formatTitle():
    """
    Checks the formatting of titles
    """
    assert len(formatter.formatTitle("abc"*40)) == 43

def test_currency():
    """
    Checks the currency calculations
    """
    usd = 10
    inr = formatter.EXCHANGES["rates"]["INR"]
    eur = formatter.EXCHANGES["rates"]["EUR"]
    aud = formatter.EXCHANGES["rates"]["AUD"]
    yen = formatter.EXCHANGES["rates"]["JPY"]
    pound = formatter.EXCHANGES["rates"]["GBP"]

    assert formatter.getCurrency("inr", "$10.00") == "INR " + str(round(usd*inr, 2))
    assert formatter.getCurrency("euro", "$10.00") == "EURO " + str(round(usd*eur, 2))
    assert formatter.getCurrency("aud", "$10.00") == "AUD " + str(round(usd*aud, 2))
    assert formatter.getCurrency("yen", "$10.00") == "YEN " + str(round(usd*yen, 2))
    assert formatter.getCurrency("pound", "$10.00") == "POUND " + str(round(usd*pound, 2))
