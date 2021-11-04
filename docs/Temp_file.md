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
```--currency``` 
Example:
```
For Mac
python3 slash.py --search "socks" --currency "inr"

For Windows
python slash.py --search "socks" --currency "inr"

```


#### 5. Save products in csv
```--currency``` accepts one or more arguments that helps the user choose their desired currency for the product price.
Example:
```
For Mac
python3 slash.py --search "socks" --currency "inr"

For Windows
python slash.py --search "socks" --currency "inr"

```


#### 6. View Excel sheet in cmd line
```--currency``` accepts one or more arguments that helps the user choose their desired currency for the product price.
Example:
```
For Mac
python3 slash.py --search "socks" --currency "inr"

For Windows
python slash.py --search "socks" --currency "inr"

```
