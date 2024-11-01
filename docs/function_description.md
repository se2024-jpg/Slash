## **slash.py**
### *def main()*: 
Provides help for every argument

## **scaper.py**

### *def searchBestbuy(query, df_flag, currency)*:
The searchBestbuy function scrapes bestbuy.com using the scraping\
**Parameters**:\
query- search query for the product\
df_flag- flag variable\
currency- currency type entered by the user

### *def searchEbay(query, df_flag, currency)*:
The searchEbay function scrapes ebay.com using the API\
**Parameters**:\
query- search query for the product\
df_flag- flag variable\
currency- currency type entered by the user

### *def httpsGet(URL)*: 
The httpsGet function makes HTTP called to the requested URL with custom headers

### *def searchAmazon(query, df_flag, currency)*:  
The searchAmazon function scrapes amazon.com\
**Parameters**:\
query- search query for the product\
df_flag- flag variable\
currency- currency type entered by the user

Returns a list of items available on Amazon.com that match the product entered by the user.

### *def searchWalmart(query, df_flag, currency)*:
The searchWalmart function scrapes walmart.com\
**Parameters**:\
query- search query for the product\
df_flag- flag variable\
currency- currency type entered by the user

Returns a list of items available on walmart.com that match the product entered by the user.

### *def amazon_scraper(link)*: 
The amazon scraper function scrapes amazon.com.
**Parameters**:\
link- link of the product for which price has to be fetched

Returns Updated Price from the Link

Return
### *def google_scraper(link)*: 
The google scraper function scrapes google.com.
**Parameters**:\
link- link of the product for which price has to be fetched

Returns Updated Price from the Link

### *def walmart_scraper(link)*: 
The walmart scraper function scrapes walmart.com.
**Parameters**:\
link- link of the product for which price has to be fetched

Returns Updated Price from the Link

### *def ebay_scraper(link)*: 
The ebay scraper function scrapes ebay.com.
**Parameters**:\
link- link of the product for which price has to be fetched

Returns Updated Price from the Link

### *def bestbuy_scraper(link)*: 
The ebay scraper function scrapes bestbuy.com.
**Parameters**:\
link- link of the product for which price has to be fetched

Returns Updated Price from the Link

### *def target_scraper(link)*: 
The target scraper function scrapes target.com.
**Parameters**:\
link- link of the product for which price has to be fetched

Returns Updated Price from the Link

### *def driver(product, currency, num=None, df_flag=0,csv=False,cd=None, website=None)*:
Returns csv if the user enters the --csv arg, else will display the result table in the terminal based on the args entered by the user.

### *def get_currency_rate(from_currency="USD", to_currency="USD")*:
Fetches the exchange rate from the specified from_currency to to_currency using an external API
**Parameters**:\
from_currency: The currency code to convert from (default is "USD").
to_currency: The currency code to convert to (default is "USD").
Returns-
    rate: The exchange rate from from_currency to to_currency as a float.

### *def convert_currency(amount, to_currency, rate):*
Converts a given amount from one currency to another using the provided exchange rate
**Parameters**:\
amount: The amount to be converted, as a string with optional currency symbol (e.g., "$100.00").
to_currency: The target currency code for conversion.
rate: The exchange rate to apply for the conversion.
Returns-
    A formatted string showing the converted amount in the target currency, rounded to two decimal places.

### *def condense_helper(result_condensed, list, num):*
The condense_helper function is a helper function designed to limit the number of entries in a result list.
**Parameters**:\
result_condensed: A list that will store the condensed results. This list is populated with entries from the list parameter until the specified limit (num) is reached.
list: A list of entries (dictionaries) that are being processed. Each entry is expected to have a "title" key.
num: An optional parameter that specifies the maximum number of entries to include in the result_condensed list. If num is None, there is no limit on the number of entries.

### *def filter(data, price_min = 1, price_max = 100000, rating_min = 1):*
The filter function is designed to filter a list of product entries based on specified criteria for price and rating.
**Parameters**:\
data: A list of dictionaries, where each dictionary represents a product entry. Each dictionary is expected to have keys for 'price' and 'rating'.
price_min: An optional parameter that specifies the minimum price for the products to be included in the filtered results. The default value is 1.
price_max: An optional parameter that specifies the maximum price for the products to be included in the filtered results. The default value is 100000.
rating_min: An optional parameter that specifies the minimum rating for the products to be included in the filtered results. The default value is 1.

## **formatter.py**

### *def formatResult(website, titles, prices, links,ratings,df_flag, currency)*:
The formatResult function takes the scraped HTML as input, and extracts the necessary values from the HTML code. Ex. extracting a price '$19.99' from a paragraph tag.\
**Parameters**: \
titles- scraped titles of the products\
prices- scraped prices of the products\
links- scraped links of the products on the respective e-commerce sites\
ratings-scraped ratings of the product

Returns a dictionary of all the parameters stated above for the product.

### *def sortList(arr, sortBy, reverse)*:
It sorts the products list based on the flags provided as arguements. Currently, it supports sorting by price.\
**Parameters-**\
SortBy- "pr": sorts by price, SortBy- "ra": sorts by rating

Returns- Sorted list of the products based on the parameter requested by the user

### *def formatSearchQuery(query)*:
It formats the search string into a string that can be sent as a url paramenter.

### *def formatTitle(title)*:
It formats titles extracted from the scraped HTML code.

### *def getNumbers(st)*:
It extracts float values for the price from a string.\
Ex. it extracts 10.99 from '$10.99' or 'starting at $10.99'

### *def getCurrency(currency, price)*:
The getCurrency function converts the prices listed in USD to user specified currency. \
Currently it supports INR, EURO, AUD, YUAN, YEN, POUND.

## full_version.py 

### *def login(self)*:
Used for User Login with password\
Returns the username.

### *def scrape(self,prod)*:
calls the scraper function from scraper.py

## csv_writer.py

### *def write_csv(arr,product,file_path)*:
Returns the CSV file with the naming nomenclature as 'ProductDate_Time'\
**Parameters**-\
product: product entered by the user\
file_path: path where the csv needs to be stored\
**Returns**-\
file_name: CSV file

## features.py

### *def usr_dir(username)*:
Returns path for user profiles 

### *def create_user(username)*:
Creates a new user if username does not exist

### *def list_users()*:
Returns lists of users

### *def create_wishlist(username, wishlist_name)*:
Creates a wishlist

### *def list_wishlists(username)*:
Listing all the wishlists for a user

### *def delete_wishlist(username, wishlist_name)*:
Deletes the mentioned wishlist

### *def wishlist_add_item(username, wishlist_name, item_data)*:
Adds the item to the wishlist

### *def read_wishlist(username, wishlist_name)*:
Returns the wishlist with all items in it

### *def wishlist_remove_list(username, wishlist_name, indx)*:
Deletes the item from the wishlist













