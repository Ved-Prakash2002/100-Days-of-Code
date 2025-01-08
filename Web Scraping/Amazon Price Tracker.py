import requests  # For making HTTP requests to fetch the webpage
from bs4 import BeautifulSoup  # For parsing and extracting information from the HTML content
import smtplib  # For sending emails

# User email credentials (add your email and password here)
my_email = ""  # Replace with your email
password = ""  # Replace with your email password

# HTTP headers to mimic a real browser and avoid being blocked by the website
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

# URL of the product webpage to monitor
URL = "https://appbrewery.github.io/instant_pot/"

# Fetch the webpage content
response = requests.get(URL)  # Make a GET request to the URL
webpage = response.text  # Get the raw HTML content of the webpage

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

# Extract the whole number part of the product price
price_whole = soup.find("span", class_="a-price-whole")
# Extract the fractional part of the product price
price_fraction = soup.find("span", class_="a-price-fraction")
# Extract the product title
product_title = soup.find("span", id="productTitle", class_="a-size-large product-title-word-break")

# Combine whole and fractional parts to get the full price as a float
current_price = float(price_whole.get_text() + price_fraction.get_text())

# Get the product title as text
product_title_text = product_title.get_text()

# Format the product title by splitting and joining to remove extra spaces
product_title_split = product_title_text.split()
product_title_formatted = ' '.join(product_title_split)

# Target price for triggering an alert
target_price = 100  # Replace with your desired price threshold

# Check if the current price is below the target price
if current_price < target_price:
    # Send an email alert using SMTP if the price is below the target
    with smtplib.SMTP("smtp.gmail.com") as connection:  # Connect to Gmail's SMTP server
        connection.starttls()  # Start a secure TLS connection
        connection.login(my_email, password)  # Log in to the email account
        # Compose the email message
        message = (f"Price is below $100\n"
                   f"Product Title: {product_title_formatted}\n"
                   f"Product Link: {URL}\n"
                   f"Current_price: ${current_price}")
        # Send the email
        connection.sendmail(from_addr=my_email,
                            to_addrs="",  # Replace with recipient email address
                            msg=message.encode("utf-8"))
    connection.close()  # Close the connection to the SMTP server
