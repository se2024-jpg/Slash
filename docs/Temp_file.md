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



#### 7
C:\Anant\NCSU\GITHUB\slash\src>python slash.py --search "socks" --csv --cd C:\Anant\NCSU\slash_test_csv
CSV Saved at:  C:\Anant\NCSU\slash_test_csv
File Name: C:\Anant\NCSU\slash_test_csv\socks211104_1223.csv


             timestamp                                    title   price                                     link  website  rating
0  04/11/2021 12:23:00  CelerSport 6 Pack Men's Ankle Socks ...  $15.95  www.amazon.com/gp/slredirect/picasso...   amazon     4.7
1  04/11/2021 12:23:00  Men's 6 Pack Everyday Kit Cushioned ...  $12.99  www.amazon.com/gp/slredirect/picasso...   amazon     4.6
2  04/11/2021 12:23:00  mens Dual Defense Cushioned Socks - ...  $11.97  www.amazon.com/Fruit-Loom-Cushion-De...   amazon     4.7
3  04/11/2021 12:23:02  Hanes Women's Cool Comfort Ankle Soc...  $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart     4.2
4  04/11/2021 12:23:02  Hanes Women's Cool Comfort Crew Sock...  $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart     4.2
5  04/11/2021 12:23:02  AND1 Men's Cushion No Show Socks, 12...  $11.47  www.walmart.comhttps://wrd.walmart.c...  walmart     4.6
6  04/11/2021 12:23:03      5socks /set -  Cotton Women's Socks  $16.00  www.Etsy.comhttps://www.etsy.com/lis...     Etsy     5.0
7  04/11/2021 12:23:03  Follkee Women's Alpaca Wool Socks Pe...  $18.49  www.Etsy.comhttps://www.etsy.com/lis...     Etsy     5.0
8  04/11/2021 12:23:03                  Great White Shark Socks  $11.95  www.Etsy.comhttps://www.etsy.com/lis...     Etsy     5.0



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
1
Enter name of product to Search: socks
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
11   04/11/2021 12:24:24  Mens Dual Defense Cushioned No Show ...      $11.99  www.amazon.com/Fruit-Loom-Defense-So...   amazon    4.7
12   04/11/2021 12:24:24          Women's 6-Pack Casual Crew Sock      $12.90  www.amazon.com/Amazon-Essentials-Wom...   amazon    4.6
13   04/11/2021 12:24:24  CelerSport 6 Pack Men's Ankle Socks ...      $15.95  www.amazon.com/CelerSport-Running-At...   amazon    4.7
14   04/11/2021 12:24:24  Men's Max Cushion Crew Socks, 6-Pair...       $9.98  www.amazon.com/Hanes-ComfortBlend-Cu...   amazon    4.6
15   04/11/2021 12:24:24  Men's Multi-Pack Mesh Ventilating Co...      $13.99  www.amazon.com/Saucony-Ventilating-P...   amazon    4.6
16   04/11/2021 12:24:24  Women's Cushioned Anti Skid Non-Slip...      $12.99  www.amazon.com/gp/slredirect/picasso...   amazon      4
17   04/11/2021 12:24:24  No Show Men Socks, Low Cut Ankle Soc...      $18.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.5
18   04/11/2021 12:24:24  Women Winter Socks Women Socks Warm ...      $12.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.6
19   04/11/2021 12:24:24  Men's All Purpose Cushion Crew Socks...      $10.00  www.amazon.com/Dickies-6-Pair-Cushio...   amazon    4.5
20   04/11/2021 12:24:24  10 Pairs Mens Ankle Socks Men 10 Pac...      $17.99  www.amazon.com/COOVAN-Pairs-Comfort-...   amazon    4.7
21   04/11/2021 12:24:24  Women's Dri-tech Moisture Control Cr...      $14.00  www.amazon.com/Dickies-Dritech-Advan...   amazon    4.7
22   04/11/2021 12:24:24  5 Pairs Womens Wool Socks Thick Knit...      $18.99  www.amazon.com/Loritta-Womens-Winter...   amazon    4.6
23   04/11/2021 12:24:24  mens Dri-tech Moisture Control Quart...      $12.99  www.amazon.com/Dickies-Multi-Pack-Dr...   amazon    4.7
24   04/11/2021 12:24:24  mens Double Crew Socks 12-pair Pack,...      $16.99  www.amazon.com/Hanes-12-Pack-FreshIQ...   amazon    4.7
25   04/11/2021 12:24:24         Adult Cotton Crew Socks, 6-Pairs      $20.23  www.amazon.com/Under-Armour-Charged-...   amazon    4.7
26   04/11/2021 12:24:24  Women's 10-Pair Value Pack No Show S...       $8.79  www.amazon.com/Hanes-Womens-Show-10-...   amazon    4.6
27   04/11/2021 12:24:24  10 Pairs Ankle Socks No Show Sock Lo...      $11.95  www.amazon.com/Moisture-Athletic-Inv...   amazon    4.3
28   04/11/2021 12:24:24  Men's 10-Pack Cotton Half Cushioned ...      $21.80  www.amazon.com/Amazon-Essentials-Sta...   amazon    4.6
29   04/11/2021 12:24:24  CelerSport 6 Pack Men's Running Ankl...      $15.95  www.amazon.com/CelerSport-Running-An...   amazon    4.7
30   04/11/2021 12:24:24  6-pk. Performance Cotton Crew Socks ...      $34.50  www.amazon.com/Nike-6-pk-Performance...   amazon    4.7
31   04/11/2021 12:24:24  Warm Socks, Taotique 5 Pairs Women W...      $15.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.5
32   04/11/2021 12:24:24  6 Pair Funky Socks, Whatever Socks, ...      $14.99  www.amazon.com/gp/slredirect/picasso...   amazon      5
33   04/11/2021 12:24:24  mens Dual Defense Cushioned Socks - ...      $11.97  www.amazon.com/gp/slredirect/picasso...   amazon    4.7
34   04/11/2021 12:24:24  Men's 656s Cotton Crew Athletic Sock...      $20.00  www.amazon.com/Gold-Toe-656S-Athleti...   amazon    4.7
35   04/11/2021 12:24:24  Men's Polyester Half Cushion Crew So...      $15.00  www.amazon.com/Gildan-Polyester-Cush...   amazon    4.6
36   04/11/2021 12:24:24  Men's FreshIQ, X-Temp Cushioned Foot...      $13.46  www.amazon.com/Hanes-Mens-Active-12-...   amazon    4.7
37   04/11/2021 12:24:24   Men's Superlite No Show Socks (6-pair)      $18.61  www.amazon.com/adidas-Superlite-Sock...   amazon    4.7
38   04/11/2021 12:24:24   Women's 10-Pair Value Pack Ankle Socks      $10.47  www.amazon.com/Hanes-Cushioned-Women...   amazon    4.7
39   04/11/2021 12:24:24  Women's 10-Pair Value Pack Low Cut S...      $10.47  www.amazon.com/10-Cushioned-Womens-A...   amazon    4.7
40   04/11/2021 12:24:24  Men's FreshIQ X-Temp Active Cool Cre...      $13.46  www.amazon.com/Hanes-Active-12-Pack-...   amazon    4.7
41   04/11/2021 12:24:24          womens Active 6 Pair Pack Socks       $7.47  www.amazon.com/Fruit-Loom-Womens-6-P...   amazon    4.7
42   04/11/2021 12:24:24           Kids' 10-Pack Cotton Crew Sock      $10.50  www.amazon.com/Amazon-Essentials-10-...   amazon    4.6
43   04/11/2021 12:24:24  mens Dri-tech Moisture Control Comfo...      $14.00  www.amazon.com/Dickies-Dri-Tech-Mois...   amazon    4.7
44   04/11/2021 12:24:24  Men's Multi-Pack Mesh Ventilating Co...      $13.85  www.amazon.com/Saucony-Multi-Pack-Ve...   amazon    4.7
45   04/11/2021 12:24:24  mens Athletic Cushioned Low Cut Sock...      $20.00  www.amazon.com/adidas-Cushioned-Athl...   amazon    4.7
46   04/11/2021 12:24:24      Mens Value 10 Pack Ankle Crew Socks      $16.99  www.amazon.com/Fruit-Loom-Value-Ankl...   amazon    4.5
47   04/11/2021 12:24:24  Adult Performance Tech No Show Socks...      $22.00  www.amazon.com/Under-Armour-Adult-Pe...   amazon    4.7
48   04/11/2021 12:24:24  Graduated Medical Compression Socks ...      $18.95  www.amazon.com/Graduated-Medical-Com...   amazon    4.4
49   04/11/2021 12:24:24  Moisture Control Crew Sock 4 Pack, M...      $12.99  www.amazon.com/Columbia-Moisture-Con...   amazon    4.6
50   04/11/2021 12:24:24            Women's Mini Crew Sock 6-Pack      $14.62  www.amazon.com/Womens-Mini-Crew-6-Pa...   amazon    4.7
51   04/11/2021 12:24:24         mens Trefoil Crew Socks (6-pair)      $20.00  www.amazon.com/adidas-Originals-Tref...   amazon    4.8
52   04/11/2021 12:24:24  Men`s Ankle Socks, 186V12,12-Pack, 1...      $13.46  www.amazon.com/Hanes-Men%60s-Ankle-1...   amazon    4.6
53   04/11/2021 12:24:24  Mens Ankle Socks Athletic Cushioned ...      $14.99  www.amazon.com/Cooplus-Athletic-Cush...   amazon    4.7
54   04/11/2021 12:24:24  Men's 6-Pack Performance Cotton Cush...      $16.00  www.amazon.com/Amazon-Essentials-Per...   amazon    4.5
55   04/11/2021 12:24:24  mens Stretch Cotton Half Cushion No ...      $10.97  www.amazon.com/Gildan-Stretch-Cotton...   amazon    4.6
56   04/11/2021 12:24:24  Women's Selective Cushion Performanc...      $13.99  www.amazon.com/Saucony-Womens-Perfor...   amazon    4.7
57   04/11/2021 12:24:24  Adult Performance Tech Low Cut Socks...      $22.00  www.amazon.com/Under-Armour-Adult-Pe...   amazon    4.7
58   04/11/2021 12:24:24  Women's 6-Pack Performance Cotton Cu...      $17.70  www.amazon.com/gp/slredirect/picasso...   amazon    4.5
59   04/11/2021 12:24:24  Warm Thermal Wool Socks for Winter M...      $19.96  www.amazon.com/gp/slredirect/picasso...   amazon    4.8
60   04/11/2021 12:24:24  Men's Running Crew Socks 6 Pairs Cot...      $21.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.7
61   04/11/2021 12:24:24  Men's Athletic Ankle Socks 8 Pairs T...      $22.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.6
62   04/11/2021 12:24:25  Hanes Women's Cool Comfort Ankle Soc...      $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
63   04/11/2021 12:24:25  Hanes Women's Cool Comfort Crew Sock...      $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
64   04/11/2021 12:24:25  AND1 Men's Cushion No Show Socks, 12...      $11.47  www.walmart.comhttps://wrd.walmart.c...  walmart    4.6
65   04/11/2021 12:24:25  Gildan Adult Men's Performance Cotto...      $10.00  www.walmart.comhttps://wrd.walmart.c...  walmart    4.3
66   04/11/2021 12:24:25  Hanes Women's Cool Comfort No Show S...      $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.4
67   04/11/2021 12:24:25  Avia Women's Performance Flatknit Lo...       $9.97  www.walmart.com/ip/Avia-Women-s-Perf...  walmart      5
68   04/11/2021 12:24:25  Athletic Works Men's Ankle Socks 12 ...       $9.97  www.walmart.com/ip/Athletic-Works-Me...  walmart    4.4
69   04/11/2021 12:24:25  Athletic Works Men's Crew Socks 12 Pack       $9.97  www.walmart.com/ip/Athletic-Works-Me...  walmart    4.5
70   04/11/2021 12:24:25  Hanes Women's Cool Comfort Sport Ank...  From $8.97  www.walmart.com/ip/Hanes-Women-s-Com...  walmart    4.5
71   04/11/2021 12:24:25  Hanes Women's Cool Comfort No Show S...  From $5.99  www.walmart.com/ip/Hanes-Women-s-Com...  walmart    4.5
72   04/11/2021 12:24:26  Follkee Women's Alpaca Wool Socks Pe...      $18.49  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
73   04/11/2021 12:24:26  Alpaca Socks | GoWith 2 Pairs Cozy W...      $19.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
74   04/11/2021 12:24:26                  Great White Shark Socks      $11.95  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
75   04/11/2021 12:24:26  Miss June’s| 1 Pair Cashmere Wool bl...      $15.00  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
76   04/11/2021 12:24:26  Custom Face Socks w Text, Personaliz...       $7.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
77   04/11/2021 12:24:26  Customized Dog Socks - Put Your Cute...       $8.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
78   04/11/2021 12:24:26  Follkee Women's Alpaca Wool Socks Pe...      $18.49  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
79   04/11/2021 12:24:26  Custom Pet Socks - Dog Socks For Men...       $9.88  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
80   04/11/2021 12:24:26  PDF Knitting Pattern Crikey Crocodil...       $7.50  www.Etsy.comhttps://www.etsy.com/lis...     Etsy    4.5
81   04/11/2021 12:24:26  5 PAIRS of Cashmere Wool Blend Socks...      $34.36  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
82   04/11/2021 12:24:26  Custom Pet Socks, Dog Socks, Pup Soc...       $7.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
83   04/11/2021 12:24:26  Warm & Cozy Cupcake Socks, Sleeping,...       $4.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
84   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
85   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
86   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
87   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
88   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
89   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
90   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
91   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
92   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
93   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
94   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
95   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
96   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
97   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
98   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
99   04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
100  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
101  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
102  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
103  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
104  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
105  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
106  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
107  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
108  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
109  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
110  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
111  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
112  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
113  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
114  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
115  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
116  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
117  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
118  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
119  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
120  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
121  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
122  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
123  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
124  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
125  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
126  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
127  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
128  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
129  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
130  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
131  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
132  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
133  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
134  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy
135  04/11/2021 12:24:26                                                    $  www.Etsy.comhttps://www.etsy.com/lis...     Etsy


Enter 1 to save product to list
2 to open link in browser
else enter any other key to continue
1
Enter row number of product to save: 4
             timestamp                                  title  price                                     link website rating
4  04/11/2021 12:24:24  Women's 10-Pair Value Pack Crew Socks  $8.79  www.amazon.com/Hanes-Womens-Crew-Whi...  amazon    4.7
Select from following:
1. Search new product
2. See exiting list
3. See Currency Conversion
4. Exit
2
             timestamp                                  title  price                                     link website  rating
0  04/11/2021 12:24:24  Women's 10-Pair Value Pack Crew Socks  $8.79  www.amazon.com/Hanes-Womens-Crew-Whi...  amazon     4.7
Select from the following:
1. Delete item from list
2. Open link in Chrome
3. Continue
2
Enter row number to open in chrome: 0
Select from following:
1. Search new product
2. See exiting list
3. See Currency Conversion
4. Exit
4
Thank You for Using Slash
