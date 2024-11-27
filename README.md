# Slash 2.0

Slash Your Spending, Not Your Style - Smarter Shopping, Personalized Just for You!

<p align="center"><img width="500" src="./assets/Shop.gif"></p>

[![GitHub license](https://img.shields.io/github/license/CSC510-SE-Fall2024/Team-82_Project-2)](https://github.com/CSC510-SE-Fall2024/Team-82_Project-2/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14214951.svg)](https://doi.org/10.5281/zenodo.14214951)
![Github](https://img.shields.io/badge/language-python-red.svg)
[![Run Tests On Push](https://github.com/se2024-jpg/Slash/actions/workflows/unit_test.yml/badge.svg)](https://github.com/se2024-jpg/Slash/actions/workflows/unit_test.yml)
[![codecov](https://codecov.io/gh/se2024-jpg/Slash/graph/badge.svg?token=a189jglJHB)](https://codecov.io/gh/se2024-jpg/Slash)
[![Lint Python](https://github.com/se2024-jpg/Slash/actions/workflows/pylint.yml/badge.svg)](https://github.com/se2024-jpg/Slash/actions/workflows/pylint.yml)
[![Close as a feature](https://github.com/se2024-jpg/Slash/actions/workflows/close_as_a_feature.yml/badge.svg)](https://github.com/se2024-jpg/Slash/actions/workflows/close_as_a_feature.yml)
[![Python Application](https://github.com/se2024-jpg/Slash/actions/workflows/python-package.yml/badge.svg)](https://github.com/se2024-jpg/Slash/actions/workflows/python-package.yml)
[![Python Style Checker](https://github.com/se2024-jpg/Slash/actions/workflows/style_checker.yml/badge.svg)](https://github.com/se2024-jpg/Slash/actions/workflows/style_checker.yml)
[![CodeQL](https://github.com/se2024-jpg/Slash/actions/workflows/codeql.yml/badge.svg)](https://github.com/se2024-jpg/Slash/actions/workflows/codeql.yml)
[![Running Code Coverage](https://github.com/se2024-jpg/Slash/actions/workflows/code_cov.yml/badge.svg)](https://github.com/se2024-jpg/Slash/actions/workflows/code_cov.yml)
[![GitHub issues](https://img.shields.io/github/issues/se2024-jpg/Slash)](https://github.com/se2024-jpg/Slash/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/se2024-jpg/Slash)](https://github.com/se2024-jpg/Slash/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/se2024-jpg/Slash)](https://github.com/se2024-jpg/Slash/pulls?q=is%3Apr+is%3Aclosed)
![Last Commit](https://img.shields.io/github/last-commit/se2024-jpg/Slash)

<a href="https://github.com/se2024-jpg/Slash/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/se2024-jpg/Slash?cacheBuster=1"></a>
<a href="https://github.com/se2024-jpg/Slash/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/se2024-jpg/Slash?cacheBuster=1"></a>

Slash is a tool that scrapes the most popular e-commerce websites to get the best deals on searched items across these websites.
Currently supported websites include [Walmart](https://www.walmart.com/), [Target](https://www.target.com/), [BestBuy](https://www.bestbuy.com/), [Amazon](https://www.amazon.com/), [Google Shopping](https://shopping.google.com/), [Etsy](https://www.etsy.com/), and [EBay](https://www.ebay.com/).

- **Fast**: With slash, you can save over 50% of your time by comparing deals across websites within seconds
- **Easy**: Slash uses very easy commands to filter, sort and search your items
- **Powerful**: Quickly alter the commands to get desired results

# :thought_balloon: Use Case

- **_Students_**: Students coming to university are generally on a budget and time constraint and generally spend hours wasting time to search for products on Websites. Slash is the perfect tool for these students that slashes all the unnecessary details on a website and helps them get prices for a product across multiple websites.Make the most of this tool in the upcoming Black Friday Sale.
- **_Data Analysts_**: Finding data for any project is one of the most tedious job for a data analyst, and the datasets found might not be the most recent one. Using slash, they can create their own dataset in real time and format it as per their needs so that they can focus on what is actually inportant.

# :rocket: Quick Guide

1. Access the Github repository from your computer.

- First, pre-install [git](https://git-scm.com/) on your machine.
- Then, clone the repo using the following command:

```
git clone https://github.com/se2024-jpg/Slash.git
```

- Finally, `cd` into the local repository.

```
cd slash
```

2. Run the installation script `install.py`:

- Execute the `install.py` script to handle all setup requirements automatically. This includes installing dependencies, setting up environment variables, and ensuring the project is ready to run.
- The script will prompt you for the following inputs Google OAuth Client ID, Google OAuth Client Secret, Google Email ID, Google Email Password. These inputs are handled securely.

```
python3 install.py
```

3. Run the project

- After installation, start the Flask application:

```
flask run
```

4. Access the application

- Open your web browser and navigate to:

```
http://localhost:5000
```

<p>


## 🔑 **Setting up Google OAuth Login**

Follow these steps to configure and enable Google OAuth login:

### 1️⃣ **Create a Google OAuth App**

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the necessary APIs:

   - Go to **APIs & Services > Library**.
   - Search for **Google Identity API** and enable it.

4. **Set up the OAuth Consent Screen**:

   - Navigate to **APIs & Services > OAuth consent screen**.
   - Choose **External** as the User Type.
   - Provide essential details like **App Name**, **Support Email**, and **Developer Contact Info**.
   - Add OAuth scopes:
     - `email`
     - `profile`
     - `openid`
   - Save and **Publish** the consent screen.

5. **Create OAuth Credentials**:
   - Go to **APIs & Services > Credentials**.
   - Click **Create Credentials > OAuth Client ID**.
   - Choose **Web Application** as the Application Type.
   - Add an **Authorized Redirect URI**:  
     `http://localhost:5000/google/callback`
   - Save the **Client ID** and **Client Secret** for use in your application while running install.py file.

---
 
# :dizzy: What's New? (Slash 2.0 Updates)

Slash 2.0 introduces a variety of new features and improvements aimed at enhancing user experience, security, and overall functionality. Below is a detailed breakdown of the key updates:

### **1. Enhanced Security: Two-Factor Authentication (2FA)**
- **Two-Factor Authentication (2FA)**:
  - Slash 2.0 now supports 2FA for a more secure login process.
  - Users will receive an OTP (One-Time Password) via email, which must be entered to verify their identity.
  - This additional layer of security ensures that only authorized users can access their accounts.

### **2. Data Security: Migration to a Secure Database**
- **Database Migration**:
  - All data, including user credentials and product details, has been migrated from `.csv` files to a secure, centralized database.
  - This move ensures better performance, scalability, and more robust data protection.

### **3. User Interface: UI Overhaul**
- **UI Refresh**:
  - Slash 2.0 introduces a completely redesigned user interface.
  - The new interface is more intuitive, modern, and user-friendly, improving overall navigation and accessibility.

### **4. Voice Search: Hands-Free Product Search**
- **Voice Search Functionality**:
  - Slash 2.0 now supports voice search through speech-to-text technology.
  - Users can perform searches hands-free, improving convenience and speeding up the search process.

### **5. Product Tracking: Wishlist and Price Drop Alerts**
- **Wishlist**:
  - Users can now save products to a Wishlist for future reference.
  - This allows users to easily track and revisit items they are interested in buying later.

- **Price Drop Alerts**:
  - Slash 2.0 now sends notifications when the price of a product drops.
  - Users are alerted when items they are interested in become more affordable, helping them to grab the best deals.

### **6. Product Comparison: Side-by-Side Product Analysis**
- **Product Comparison**:
  - Users can now compare specific products across various e-commerce websites.
  - This feature allows side-by-side comparisons of product specifications, prices, and availability, helping users make more informed purchase decisions.

### **7. Search Insights: Visualization Bar**
- **Visualization Bar**:
  - Slash 2.0 introduces a visualization bar that provides insights into the search results.
  - The bar displays the number of products found across different platforms like Walmart, Amazon, eBay, etc., giving users an overview of the search breadth.

### **8. AI-Powered Recommendations**
- **Product Recommendations**:
  - Slash 2.0 leverages artificial intelligence to recommend products based on previous searches.
  - These personalized suggestions help users discover related products they may not have encountered otherwise, improving the shopping experience.

### **9. Simplified Installation and Secure API Management**
- **Simplified Installation**:
  - Slash 2.0 features an easier and more organized installation procedure.
  - The new setup process allows users to quickly install and configure the application with minimal steps.

- **Secure API Management**:
  - API keys and credentials are now managed in a more secure way during installation.
  - This ensures sensitive data is protected, following best practices for handling API keys securely.





## :movie_camera: Checkout our demo video

[![Video](https://img.youtube.com/vi/5iCc2LJa_bI/0.jpg)](https://youtu.be/5iCc2LJa_bI)

# :muscle: What's next for future development?

### 1. Real-Time Notification System
- **Real-Time Price Alerts**: Implement real-time notifications that alert users when a product on their wishlist or tracked products has its price drop or when a limited-time deal becomes available.
- **Email and SMS Notifications**: Users can opt to receive notifications via email or SMS for important updates, such as a price drop, availability change, or when a product becomes eligible for a deal.
- **Push Notifications for New Deals**: Enable push notifications within the app to notify users of new deals based on their search preferences or previously tracked products.

### 2. Predictive Pricing Algorithms
- **Dynamic Price Prediction**: Develop a predictive pricing model that estimates whether the price of a product will increase or decrease over time based on historical price data and market trends.
- **Price Drop Prediction**: Implement machine learning to predict potential future price drops, alerting users when they should buy based on the likelihood of price changes.
- **Market Demand Predictions**: Analyze market demand and historical trends to forecast the best times to buy specific products, helping users make informed purchasing decisions.

### 3. Enhanced Data Storage and Management
- **Distributed Data Storage**: Implement distributed data storage solutions like NoSQL databases (e.g., MongoDB, Cassandra) to efficiently handle the growing amount of user data, product listings, and price history.
- **Data Archiving and Retrieval**: Use data archiving techniques to store old price data, ensuring fast access to historical information without compromising system performance.
- **User Behavior Data Analytics**: Store and analyze user interaction data to generate insights into user preferences, helping tailor product recommendations and improve user experience.

### 4. Cloud-Native Infrastructure
- **Serverless Computing for Price Scraping**: Move to serverless architecture (e.g., AWS Lambda, Google Cloud Functions) to handle product scraping dynamically. This will allow Slash to scale without the need for dedicated server management, especially during peak traffic periods.
- **Cloud Load Balancing**: Use load balancing services to distribute traffic across multiple servers, ensuring Slash remains highly available and can handle large numbers of concurrent users without slowdown.
- **Cloud-based Caching**: Implement caching mechanisms (e.g., Redis or Memcached) in the cloud to store frequently accessed data like product prices, reducing latency and improving response time.

### 5. Containerization and Kubernetes
- **Containerization with Docker**: Containerize Slash using Docker to simplify development, testing, and deployment. This ensures consistent environments across all stages of development, making scaling easier.
- **Orchestration with Kubernetes**: Use Kubernetes to manage containers in production, ensuring efficient scaling, self-healing (auto-scaling and restarting), and better resource allocation for handling traffic spikes.
- **Microservices Architecture**: Break Slash into microservices (e.g., for user authentication, product tracking, price comparison) to allow independent scaling and development of different features.

### 6. AI-Powered Deal Prediction
- **Deal Prediction and Smart Alerts**: Using AI, predict when certain products might go on sale and send smart alerts to users, recommending the best time to purchase a product based on historical price data.

### 7. Multi-Platform Integration
- **Browser Extension**: Develop a browser extension that allows users to track product prices directly while shopping on e-commerce platforms like Amazon, Walmart, or eBay. Users can add products to their wishlist, set price alerts, and compare prices on the go.
- **Mobile App Expansion**: Expand Slash’s functionality with native mobile applications for iOS and Android, enabling users to access price comparisons, track deals, and receive notifications directly on their phones.

### 8. Smart Inventory and Product Availability Monitoring
- **Real-Time Stock Monitoring**: Integrate with e-commerce platforms to track product availability in real-time, alerting users when items are back in stock or when new deals are available.
- **Low Stock Alerts**: Notify users when a product they are interested in is low on stock or has limited availability, ensuring they don't miss out on deals.
- **Automatic Reordering**: For users who consistently track certain products, offer automatic reorder options when a product price drops or becomes available.


## Score Card
---
#### Total Grade: 145

| Factor | Score | Notes |
| --- | --- | --- |
| Video | 3 | Link Updated (https://www.youtube.com/watch?v=Fp7tj_xCvBc) |
| Workload | 3 | Distributed |
| Number of commits | 3 | 50+ |
| Number of commits: by different people | 3 | https://github.com/CSC510-SE-Fall2024/Team-82_Project-2/graphs/contributors?from=28%2F09%2F2024 |
| Issues report: There are many | 2 | https://github.com/CSC510-SE-Fall2024/Team-82_Project-2/pulse |
| Issues are being closed | 2 | https://github.com/CSC510-SE-Fall2024/Team-82_Project-2/pulse |
| DOI badge | 3 |  |
| Docs: format | 3 |  |
| Docs: description  | 3 |  |
| Docs: short animated video | 2 |  |
| Docs: strong punchlines | 3 |  |
| Docs: mini tutorials | 3 |  |
| Use of version control tools | 2 |  |
| Use of style checkers | 3 |  |
| Use of code formatters. | 3 |  |
| Use of syntax checkers. | 3 |  |
| Use of code coverage | 3 |  |
| Other automated analysis tools | 2 |  |
| Test cases exist | 3 |  |
| Test cases are routinely executed | 2 |  |
| The files http://contributing.md/ lists coding standards and lots of tips | 3 |  |
| Issues are discussed before they are closed | 3 |  |
| Chat channel: exists | 3 |  |
| Test cases: a large proportion of the issues related to handling failing cases. | 2 |  |
| Evidence that the whole team is using the same tools | 3 |  |
| Evidence that the members of the team are working across multiple places in the code base | 2 |  |
| Short release cycles | 3 |  |
| Does your website and documentation provide a clear, high-level overview of your software? | 3 |  |
| Does your website and documentation clearly describe the type of user who should use your software? | 3 |  |
| Do you publish case studies to show how your software has been used by yourself and others? | 3 |  |
| Is the name of your project/software unique? | 3 |  |
| Is your project/software name free from trademark violations? | 2 |  |
| Is your software available as a package that can be deployed without building it? | 3 |  |
| Is your software available for free? | 3 |  |
| Is your source code publicly available to download, either as a downloadable bundle or via access to a source code repository? | 3 |  |
| Is your software hosted in an established, third-party repository like GitHub? | 3 |  |
| Is your documentation clearly available on your website or within your software? | 3 |  |
| Does your documentation include a "quick start" guide, that provides a short overview of how to use your software with some basic examples of use? | 2 |  |
| If you provide more extensive documentation, does this provide clear, step-by-step instructions on how to deploy and use your software? | 3 |  |
| Do you provide a comprehensive guide to all your software’s commands, functions and options? | 3 |  |
| Do you provide troubleshooting information that describes the symptoms and step-by-step solutions for problems and error messages? | 3 |  |
| If your software can be used as a library, package or service by other software, do you provide comprehensive API documentation? | 3 |  |
| Do you store your documentation under revision control with your source code? | 2 |  |
| Do you publish your release history e.g. release data, version numbers, key features of each release etc. on your web site or in your documentation? | 3 |  |
| Does your software describe how a user can get help with using your software? | 3 |  |
| Does your website and documentation describe what support, if any, you provide to users and developers? | 3 |  |
| Does your project have an e-mail address or forum that is solely for supporting users? | 3 |  |
| Are e-mails to your support e-mail address received by more than one person? | 3 |  |
| Does your project have a ticketing system to manage bug reports and feature requests? | 2 |  |
| Is your project's ticketing system publicly visible to your users, so they can view bug reports and feature requests? | 3 |  |

# Additional Information

For Additional Information direct to this [page](https://github.com/se2024-jpg/Slash/tree/Features/docs) and check all the markdown files

# Chat Channel

<code><a href="https://discord.gg/xztHmAnM" target="_blank"><img height="100" width="250" src="https://user-images.githubusercontent.com/42767118/135394825-26dee6db-7a64-4e3f-902a-1e35abd4cf0c.png"></a></code>

## :sparkles: Contributors

<table>
  <tr>
    <td align="center"><a href="https://github.com/girish1430"><img src="https://avatars.githubusercontent.com/u/57136088?v=4" width="75px;" alt=""/><br /><sub><b>Girish G N</b></sub></a></td>
    <td align="center"><a href="https://github.com/joeljogy"><img src="https://avatars.githubusercontent.com/u/28514673?v=4" width="75px;" alt=""/><br /><sub><b>Joel Jogy George</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/prav29"><img src="https://avatars.githubusercontent.com/u/38226613?v=4" width="75px;" alt=""/><br /><sub><b>Pravallika Vasireddy</b></sub></a><br /></td>
  </tr>
</table>

## :email: Support

For support and inquiries related to **Slash 2.0**, please contact us at **csc510group77@gmail.com**. We are here to assist you and address any questions or issues you may have.

We appreciate your interest and look forward to providing you with the best possible support and updates.
