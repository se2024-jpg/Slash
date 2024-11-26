'''
MIT License

Copyright (c) 2024 Girish G N, Joel Jogy George, Pravallika Vasireddy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from src.modules.formatter import formatSearchQuery, formatTitle

def test_formatSearchQuery():
    """
    Checks the formatSearchQuery function
    """
    assert formatSearchQuery("1 2") == "1+2"
    assert formatSearchQuery("A B") == "A+B"
    assert formatSearchQuery("ABC") == "ABC"

def test_formatTitle():
    """
    Checks the formatTitle function
    """
    assert formatTitle("0"*50) == "0"*40+"..."
    assert formatTitle("0"*5) == "0"*5