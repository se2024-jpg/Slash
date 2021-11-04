#### 1. Sort by Rating
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
 6  03/11/2021 21:42:54  PDF Crikey Crocodile Socks Knit Animal S...  7.50     Etsy            4.5 
 7  03/11/2021 21:42:54  5socks /set -  Cotton Women's Socks          16.00    Etsy            5   
 8  03/11/2021 21:42:54  Follkee Women's Alpaca Wool Socks Perfec...  18.49    Etsy            5   


```

#### 2.Currency
```--currency``` accepts one or more arguments that helps the user choose their desired currency for the product price.
Example:
```
For Mac
python3 slash.py --search "socks" --currency "inr"

For Windows
python slash.py --search "socks" --currency "inr"

```

![image](https://user-images.githubusercontent.com/48826459/140242430-0d7d2707-095a-4a2d-86a7-c5e91b88d725.png)


#### 3. Added new e-commerce site - ETSY
A new e-commerce site 'Etsy' has been added in this project. Information such as the product type, product name, price, ratings, etc. has been scraped from the website.

Example:

![image](https://user-images.githubusercontent.com/48826459/140245385-00359c50-4e89-46ff-866d-26a5879d43d4.png)



#### 4. Main Menu 
```--full``` command is used to display the complete menu for the project. If the argument passed is "T", the Full version of the app will be displayed. If the argument passed is "F", the mini version of the app is displayed.

Example:

##### 1) When argument "F" is passed : 
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
5  04/11/2021 16:10:05  AND1 Men's Cushion No Show Socks, 12...  $11.47  www.walmart.comhttps://wrd.walmart.c...  walmart    4.6
6  04/11/2021 16:10:06  Follkee Women's Alpaca Wool Socks Pe...  $18.49  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
7  04/11/2021 16:10:06  Alpaca Socks | GoWith 2 Pairs Cozy W...  $19.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
8  04/11/2021 16:10:06                  Great White Shark Socks  $11.95  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
```

##### 2) When argument "T" is passed :
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
##### 2.b) If the user inputs 1 i.e. Search new product, the command ```--search``` will be used. The product which the user wishes to search for needs to be entered. 


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
5    04/11/2021 12:24:24  Men's Dri-tech Moisture Control Crew...      $14.99  www.amazon.com/Dickies-Multi-Pack-Dr...   amazon    4.7
6    04/11/2021 12:24:24  Women's Performance Heel Tab Athleti...      $14.99  www.amazon.com/Saucony-Womens-Perfor...   amazon    4.8
7    04/11/2021 12:24:24       Mens Cushioned Work Socks 10 Pairs      $12.10  www.amazon.com/Fruit-Loom-Everyday-S...   amazon    4.5
8    04/11/2021 12:24:24  CelerSport Ankle Athletic Running So...      $12.70  www.amazon.com/CelerSport-Ankle-Athl...   amazon    4.8
9    04/11/2021 12:24:24  mens Dual Defense Cushioned Socks - ...      $11.97  www.amazon.com/Fruit-Loom-Cushion-De...   amazon    4.7
10   04/11/2021 12:24:24  mens Athletic Cushioned Crew Socks (...      $18.99  www.amazon.com/adidas-Mens-Athletic-...   amazon    4.7
11   04/11/2021 12:24:25  Hanes Women's Cool Comfort Ankle Soc...      $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
12   04/11/2021 12:24:25  Hanes Women's Cool Comfort Crew Sock...      $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
13   04/11/2021 12:24:25  AND1 Men's Cushion No Show Socks, 12...      $11.47  www.walmart.comhttps://wrd.walmart.c...  walmart    4.6
14   04/11/2021 12:24:25  Gildan Adult Men's Performance Cotto...      $10.00  www.walmart.comhttps://wrd.walmart.c...  walmart    4.3
15   04/11/2021 12:24:25  Hanes Women's Cool Comfort No Show S...      $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.4
16   04/11/2021 12:24:25  Avia Women's Performance Flatknit Lo...       $9.97  www.walmart.com/ip/Avia-Women-s-Perf...  walmart      5
17   04/11/2021 12:24:25  Athletic Works Men's Ankle Socks 12 ...       $9.97  www.walmart.com/ip/Athletic-Works-Me...  walmart    4.4
18   04/11/2021 12:24:25  Athletic Works Men's Crew Socks 12 Pack       $9.97  www.walmart.com/ip/Athletic-Works-Me...  walmart    4.5
19   04/11/2021 12:24:25  Hanes Women's Cool Comfort Sport Ank...  From $8.97  www.walmart.com/ip/Hanes-Women-s-Com...  walmart    4.5
20   04/11/2021 12:24:25  Hanes Women's Cool Comfort No Show S...  From $5.99  www.walmart.com/ip/Hanes-Women-s-Com...  walmart    4.5
21   04/11/2021 12:24:26  Follkee Women's Alpaca Wool Socks Pe...      $18.49  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
22   04/11/2021 12:24:26  Alpaca Socks | GoWith 2 Pairs Cozy W...      $19.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
23   04/11/2021 12:24:26                  Great White Shark Socks      $11.95  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
24   04/11/2021 12:24:26  Miss June’s| 1 Pair Cashmere Wool bl...      $15.00  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
25   04/11/2021 12:24:26  Custom Face Socks w Text, Personaliz...       $7.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
26   04/11/2021 12:24:26  Customized Dog Socks - Put Your Cute...       $8.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
27   04/11/2021 12:24:26  Follkee Women's Alpaca Wool Socks Pe...      $18.49  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
28   04/11/2021 12:24:26  Custom Pet Socks - Dog Socks For Men...       $9.88  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
29   04/11/2021 12:24:26  PDF Knitting Pattern Crikey Crocodil...       $7.50  www.Etsy.comhttps://www.etsy.com/lis...     Etsy    4.5
30   04/11/2021 12:24:26  5 PAIRS of Cashmere Wool Blend Socks...      $34.36  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
31   04/11/2021 12:24:26  Custom Pet Socks, Dog Socks, Pup Soc...       $7.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
32   04/11/2021 12:24:26  Warm & Cozy Cupcake Socks, Sleeping,...       $4.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
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
2. See exiting list
3. See Currency Conversion
4. Exit
2
```
##### 2.c) Now that we know that there is an element in the list, we can select the "See existing List" option. 
```   
   timestamp                                  title  price                                     link website  rating
0  04/11/2021 12:24:24  Women's 10-Pair Value Pack Crew Socks  $8.79  www.amazon.com/Hanes-Womens-Crew-Whi...  amazon     4.7
```

With the list output, the user is also giventhe option to choose whether to delete the item from the list or to open the link for the product.

```
Select from the following:
1. Delete item from list
2. Open link in Chrome
3. Continue
2

Enter row number to open in chrome: 0

![image](https://user-images.githubusercontent.com/48826459/140417153-365d93d4-df64-4658-a016-eadcabeebf89.png)
```
```
Select from following:
1. Search new product
2. See exiting list
3. See Currency Conversion
4. Exit
4
Thank You for Using Slash
```

#### 5. Save products in csv
```--csv```  
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






