<p align="center"><img width="500" src="./assets/slash.png"></p>

[![GitHub license](https://img.shields.io/github/license/TommasU/slash)](https://github.com/TommasU/slash/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5739350.svg)](https://doi.org/10.5281/zenodo.5739350)
![Github](https://img.shields.io/badge/language-python-red.svg)
[![GitHub issues](https://img.shields.io/github/issues/TommasU/slash)](https://github.com/TommasU/slash/issues)
[![Github closes issues](https://img.shields.io/github/issues-closed-raw/TommasU/slash)](https://github.com/TommasU/slash/issues?q=is%3Aissue+is%3Aclosed)
[![Github closed pull requests](https://img.shields.io/github/issues-pr-closed/SEProjGrp5/slash)](https://github.com/TommasU/slash/pulls?q=is%3Apr+is%3Aclosed)
[![codecov](https://codecov.io/gh/TommasU/slash/branch/main/graph/badge.svg?token=JMI26I4YVU)](https://app.codecov.io/gh/TommasU/slash)
[![Pylint](https://github.com/SEProjGrp5/slash/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/TommasU/slash/actions/workflows/pylint.yml)
[![Python Style Checker](https://github.com/SEProjGrp5/slash/actions/workflows/style_checker.yml/badge.svg?branch=main)](https://github.com/TommasU/slash/actions/workflows/style_checker.yml)

Slash is a tool that scrapes the most popular e-commerce websites to get the best deals on searched items across these websites. 
- **Fast**: With slash, you can save over 50% of your time by comparing deals across websites within seconds
- **Easy**: Slash uses very easy commands to filter, sort and search your items
- **Powerful**: Quickly alter the commands to get desired results
<p align="center">
Checkout our newest Features! Mini Version and Full version now showcasing new sets of improvements.

<p align="center">
  <a href="#rocket-installation">Installation</a>
  ::
  <a href="#golf-flags-and-command-line-arguments">Flags & Args</a>
  ::
  <a href="#dizzy-whats-new-in-phase-2"> Whats new in Phase 3? </a>
  ::
  <a href="#muscle-whats-next-for-phase-3"> The future of Slash </a>
  ::
  <a href="#card_index_dividers-some-examples">Examples</a>
  ::
  <a href="#thought_balloon-use-case">Use Case</a>
  ::
  <a href="#page_facing_up-why">Why</a>
  ::
  <a href="#sparkles-contributors">Contributors</a>
    ::
  <a href="#email-support">Support</a>
  
</p>


# :rocket: Installation

1. Access the Github repository from your computer. 
 - First, pre-install [git](https://git-scm.com/) on  your machine. 
 - Then, clone the following repo:
 ```
 https://github.com/TommasU/slash.git
 ```
 * Finally, ```cd``` into the local repository.
```
cd slash
```
2. Install the ```requirements.txt```. 
- This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled.
- Install the ```requirements.txt``` file using pip.
```
pip3 install -r requirements.txt
```
3. Running the program
- ```cd``` into the ```src``` folder. 
``` 
cd src 
```
- Use the python command to run the ```slash.py``` file.
```
For Mac
python3 slash.py --search socks

For Windows
python slash.py --search socks
```
<p>


# :dizzy: What's new in Phase 3?


## :computer: User Friendly UI


Now featuring a friendly user interface for the Mini Version of SLASH including the best of a search bar and easy to read results. Interface provides options to 
- Sort results
- Change currency displayed
- Filter number of items displayed
- Prices
- Product link
- Timestamps for up to date results
- Ratings
<p align="center"><img width="700" src="./assets/slash.gif"></p>


### :key: Accesing Mini Version UI



1. After completing the <a href="#rocket-installation">Installation</a> and all project dependencies are installed. 

2. Make sure you ```cd``` into the ```src``` folder. 
3. Use the ```flask run``` command.
```
cd src

flask run
```
4. Once flask is running, open your internet browser and type ```http://127.0.0.1:5000/``` into the search bar.


### :money_with_wings: UI Features


1. SORTING: Based on rating or price.
2. CURRENCY: View prices in the currency of your choice.
3. RESULTS: Narrow your search based on Result Length.

<p align="center"><img width="150.1" src="./assets/sorting.PNG"><img width="130" src="./assets/currency.PNG"><img width="150.2" src="./assets/results.PNG"></p>

<p align="center">
Easy to view and access results
<p align="center"><img width="800" src="./assets/list.PNG"></p>

## :computer: Advanced Wishlists


Now featuring advanced wishlists in the Full Version of SLASH. For the best shopping experience now you can add, edit and delete wishlists with simple commands and flexiblity. Wishlist features include
- Adding new lists with custom names
- Display all available wishlists
- Add items to different wishlist during a search session

### :key: Accesing the Full Version SLASH

1. After completing the <a href="#rocket-installation">Installation</a> and all project dependencies are installed. 

2. Make sure you ```cd``` into the ```src``` folder. 
3. Use the ```slash.py --full T``` command.
```
python slash.py --full T
```

### :money_with_wings: Wishlist Features

<p align="center"><img width="220" src="./assets/full_intro.PNG"><img width="200" src="./assets/wishlist.PNG"></p>


## :computer: More websites, More results, More shopping

Now featuring results from Amazon, Walmart, Etsy, Google.

# :golf: The Basics, Flags  & Arguments 
---
Full Version Features:

The tool supports the following flags and command line arguments. These flags and arguments can be used to quickly filter and guide the search to get you the best results very quickly.

| Arguments | Type | Default | Description                                                                                  |
|-----------|------|---------|----------------------------------------------------------------------------------------------|
| --search  | str  | None    | The product name to be used as the search query                                              |
| --num     | int  | 3       | Maximum number of products to search                                                         |
| --sort    | str  | re      | Sort results by relevance (re) or by price (pr)                                              |
| --des     | bool | -       | Set boolean flag if results should be sorted in non-increasing order                         |
| --csv     |      | -       | Save results as CSV                                                                          |
| --full    | str  | F       | T for full version of app; F for mini version of app                                         |
| --link    |      |         | Show links in the table                                                                      |
|--currency | str  |         | Display the amount in specified currency(inr, euro, aud, yuan, yen, pound)                   |
 
:card_index_dividers: Some Examples
---

#### 1. Searching
```--search```  accepts one argument string which it uses to search and scrape the requested products on 
the e-commerce websites. So, to use this, run the python script followed by the --search argument and the 
search string. The search string should be in double quotes if it have two or more words. Example:
```
For Mac
python3 slash.py --search "socks"

For Windows
python slash.py --search "socks"
```
```
            timestamp                                    title        price                                     link  website  rating  no of ratings            trending
0    30/11/2021 15:20:42  Bedsure Sherpa Fleece Throw Blanket ...       $21.24  www.amazon.com/gp/slredirect/picasso...   amazon     4.7        55165.0         Best Seller  
2    30/11/2021 15:20:42  Quility Weighted Blanket with Soft C...       $79.99  www.amazon.com/gp/slredirect/picasso...   amazon     4.7        39501.0         Best Seller  
4    30/11/2021 15:20:42  Eddie Bauer Home Plush Sherpa Fleece...       $21.59  www.amazon.com/Eddie-Bauer-Cabin-Fla...   amazon     4.7         6985.0  Holiday Gift Guide  

```

#### 2. Sorting
```--sort``` accepts one or more arguments that determine how the tool sorts and filters the requested products
after scraping. The first value is used to initially sort and filter the results of the scraping. The arguments
following the first one are not required but will be used to further sort the filtered results. Example:
```
For Mac
python3 slash.py --search "socks" --sort ra

For Windows
python slash.py --search "socks" --sort ra
```
```
           timestamp                                       title    price   website      rating 
 0  03/11/2021 21:42:53  Hanes Women's Cool Comfort Ankle Socks, ...  $10.97   walmart         4.2 
 1  03/11/2021 21:42:53  Hanes Women's Cool Comfort Crew Socks, 1...  $10.97   walmart         4.2 
 2  03/11/2021 21:42:53  Hanes Mens FreshIQ Ankle Cushion Socks, ...  $13.46   walmart         4.2 
 3  03/11/2021 21:42:51  10 Pairs Ankle Socks No Show Sock Low-Cu...  $11.95   amazon          4.3 
 4  03/11/2021 21:42:50  Mens Cushioned Work Socks 10 Pairs           $12.10   amazon          4.5 
 5  03/11/2021 21:42:50  Women's 6-Pack Performance Cotton Cushio...  $17.70   amazon          4.5 
```
#### 3. Sort Order
The ```--des``` flag can be set to sort the requested products in a non-increasing order. This flag will be 
actually used when coupled with ```--sort```. Example:
```
For Mac
python3 slash.py --search "socks" --sort pr --des

For Windows
python slash.py --search "socks" --sort pr --des
```
```
           timestamp                                   title        price    website  rating   

 0  04/11/2021 13:18:30                                                        Etsy                
 1  04/11/2021 13:18:30                                                        Etsy                
 2  04/11/2021 13:18:30                                                        Etsy                
 3  04/11/2021 13:18:27  6-pk. Performance Cotton Crew Socks Size...  $34.38   amazon     4.7      
 4  04/11/2021 13:18:27  Men's 10 Pairs Cotton Moisture Control H...  $25.49   amazon     4.7      
 5  04/11/2021 13:18:27  Men's Dri-Tech Comfort Crew Sock             $25.45   amazon     4.8      
 6  04/11/2021 13:18:29  AND1 Men's Cushion No Show Socks, 12 Pac...  $11.47   walmart    4.6      
 7  04/11/2021 13:18:29  Hanes Women's Cool Comfort Ankle Socks, ...  $10.97   walmart    4.2      
 8  04/11/2021 13:18:29  Hanes Women's Cool Comfort Crew Socks, 1...  $10.97   walmart    4.2      
```

#### 4. Result length
The maximum number of results that are scraped from each website can be set using the ```--num``` argument. It accepts
an integer value ```n``` and then returns ```n``` results from each website. Note that tool returns a maximum of 
the value of ```n``` and the number of results on the webiste. By default this value is set to 3. Example:
```
For Mac
python3 slash.py --search "socks" --num 5

For Windows
python slash.py --search "socks" --num 5
```
```
              timestamp                                    title   price                                     link  website rating
0   04/11/2021 13:13:33  CelerSport 6 Pack Men's Ankle Socks ...  $15.95  www.amazon.com/gp/slredirect/picasso...   amazon    4.7
1   04/11/2021 13:13:33  CelerSport Ankle Athletic Running So...  $12.70  www.amazon.com/gp/slredirect/picasso...   amazon    4.8
2   04/11/2021 13:13:33  Men's Athletic Ankle Socks 8 Pairs T...  $22.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.6
3   04/11/2021 13:13:33  CelerSport 6 Pack Men's Athletic Cre...  $18.95  www.amazon.com/gp/slredirect/picasso...   amazon    4.6
4   04/11/2021 13:13:33    Women's 10-Pair Value Pack Crew Socks   $8.79  www.amazon.com/Hanes-Womens-Crew-Whi...   amazon    4.7
5   04/11/2021 13:13:36  Hanes Women's Cool Comfort Ankle Soc...  $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2

```


#### 5. Sort by Rating
```--sort``` accepts the argument "ra" that determine how the tool sorts and filters the requested products
after scraping on the basis of ratings of the product . 
Example:
```
For Mac
python3 slash.py --search "philips hue" --sort ra

For Windows
python slash.py --search "philips hue" --sort ra

```

```

           timestamp                                       title    price   website      rating 
 0  03/11/2021 21:42:53  Hanes Women's Cool Comfort Ankle Socks, ...  $10.97   walmart         4.2 
 1  03/11/2021 21:42:53  Hanes Women's Cool Comfort Crew Socks, 1...  $10.97   walmart         4.2 
 2  03/11/2021 21:42:53  Hanes Mens FreshIQ Ankle Cushion Socks, ...  $13.46   walmart         4.2 
 3  03/11/2021 21:42:51  10 Pairs Ankle Socks No Show Sock Low-Cu...  $11.95   amazon          4.3 
 4  03/11/2021 21:42:50  Mens Cushioned Work Socks 10 Pairs           $12.10   amazon          4.5 
 5  03/11/2021 21:42:50  Women's 6-Pack Performance Cotton Cushio...  $17.70   amazon          4.5 



```

#### 6.Currency
```--currency``` provides nasic currency conversion for different currencies like INR, EURO, AUD, YUAN, YEN and POUND.

Example:
```
For Mac
python3 slash.py --search "socks" --currency "inr"

For Windows
python slash.py --search "socks" --currency "inr"

```

![image](https://user-images.githubusercontent.com/48826459/140242430-0d7d2707-095a-4a2d-86a7-c5e91b88d725.png)





#### 7. Main Menu 
```--full``` command is used to display the complete menu for the project. If the argument passed is "T", the Full version of the app will be displayed. If the argument passed is "F", the mini version of the app is displayed.

Example:

##### 7.1) When argument "F" is passed : 
```
For Mac
python3 slash.py --search "socks" --full "F"

For Windows
python slash.py --search "socks" --full "F"

```
```
             timestamp                                    title   price                                     link  website rating
0  04/11/2021 16:10:02  Men's 6 Pack Everyday Kit Cushioned ...  $12.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.6
1  04/11/2021 16:10:02  Compression Athletic Crew Socks (6 P...  $19.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.4
2  04/11/2021 16:10:02  CelerSport 6 Pack Women's Ankle Runn...  $15.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.8
3  04/11/2021 16:10:05  Hanes Women's Cool Comfort Ankle Soc...  $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
4  04/11/2021 16:10:05  Hanes Women's Cool Comfort Crew Sock...  $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2

```

##### 7.2) When argument "T" is passed :
```
For Mac
python3 slash.py --search "socks" --full "T"

For Windows
python slash.py --search "socks" --full "T"

```

###### 2.a) The output window asks for user information in order to store the data in the database. It also displays the menu for the user. The user can select the product which             he/she wishes to search, check the existing list and see the currency conversion.

```
C:\Anant\NCSU\GITHUB\slash\src>python slash.py --full T
Welcome to Slash!
Please enter the following information:
Name: Anant
Email: agadodi@ncsu.edu
Welcome  Anant
Select from following:
1. Search new product
2. See exiting list
3. See Currency Conversion
4. Exit
```
##### 7.3) If the user inputs 1 i.e. Search new product, the command ```--search``` will be used. The product which the user wishes to search for needs to be entered. 


```
1
Enter name of product to Search: socks
```
```
               timestamp                                    title       price                                     link  website rating
0    04/11/2021 12:24:24  CelerSport Ankle Athletic Running So...      $12.70  www.amazon.com/gp/slredirect/picasso...   amazon    4.8
1    04/11/2021 12:24:24  CelerSport 6 Pack Men's Ankle Socks ...      $15.95  www.amazon.com/gp/slredirect/picasso...   amazon    4.7
2    04/11/2021 12:24:24  Men's 6 Pack Everyday Kit Cushioned ...      $12.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.6
3    04/11/2021 12:24:24  Compression Athletic Crew Socks (6 P...      $19.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.4
4    04/11/2021 12:24:24    Women's 10-Pair Value Pack Crew Socks       $8.79  www.amazon.com/Hanes-Womens-Crew-Whi...   amazon    4.7

```


Once the product list is displayed, the user is given the option to choose whether to save in the product or if he or she wished to open the browser and check the link.


```
Enter 1 to save product to list
2 to open link in browser
else enter any other key to continue
1
Enter row number of product to save: 4
```

Here, as the user entered 1, the product is saved in the list.

```
             timestamp                                  title  price                                     link website rating
4  04/11/2021 12:24:24  Women's 10-Pair Value Pack Crew Socks  $8.79  www.amazon.com/Hanes-Womens-Crew-Whi...  amazon    4.7
```
```
Select from following:
1. Search new product
2. Manage Wishlists
3. See Currency Conversion
4. Exit
```


#### 8. Save products in csv
```--csv``` command is used to save the complete list of the searched product in a csv format.
```--cd``` command here is used to change the directory for the csv file.
Example:
```
For Mac
python3 slash.py --search "socks" --csv --cd C:\Anant\NCSU\slash_test_csv

For Windows
python slash.py --search "socks" --csv --cd C:\Anant\NCSU\slash_test_csv

```
```
CSV Saved at:  C:\Anant\NCSU\slash_test_csv
File Name: C:\Anant\NCSU\slash_test_csv\socks211104_1223.csv
```

![image](https://user-images.githubusercontent.com/48826459/140409684-a352f30a-9b01-4369-a044-f166eab42630.png)




# :muscle: What's next for future development?

- Creating ordering and payment functionality for customers to directly order from command line
- Create an advanced user interface for full version of the program.


:thought_balloon: Use Case
---
* ***Students***: Students coming to university are generally on a budget and time constraint and generally spend hours wasting time to search for products on Websites. Slash is the perfect tool for these students that slashes all the unnecessary details on a website and helps them get prices for a product across multiple websites.Make the most of this tool in the upcoming Black Friday Sale.
* ***Data Analysts***: Finding data for any project is one of the most tedious job for a data analyst, and the datasets found might not be the most recent one. Using slash, they can create their own dataset in real time and format it as per their needs so that they can focus on what is actually inportant.

:page_facing_up: Why
---
- In a market where we are spoilt for choices, we often look for the best deals.  
- The ubiquity of internet access has leveled the retail playing field, making it easy for individuals and businesses to sell products without geographic limitation. In 2020, U.S. e-commerce sales, receiving a boost due to the COVID-19 pandemic, grew 44% and represented more than 21% of total retail sales, according to e-commerce information source Internet Retailer.
- The growth of e-commerce has not only changed the way customers shop, but also their expectations of how brands approach customer service, personalize communications, and provide customers choices.
- E-commerce market has prompted cut throat competition amongst dealers, which is discernable through the price patterns for products of major market players. Price cuts are somewhat of a norm now and getting the best deal for your money can sometimes be a hassle (even while online shopping).
- This is what Slash aims to reduce by giving you an easy to use, all in one place solution for finding the best deals for your products that major market dealers have to offer!
- Slash in its current form is for people who have some understanding of python and are comfortable in using the command line interface to interact with systems.
- Future updates aim to encompass a wide variety of users irrespective of their computer knowledge and background.


# :sparkles: Contributors

- Jessica Vargas(jrvargas)
- Parth Parikh(pmparikh)
- Radhika Toravi(rtoravi)
- Rushikesh Deodhar(rdeodha)
- Saurabh Nanda(snanda)

## :email: Support


For any queries and help, please reach out to us at: fall2021se@gmail.com
