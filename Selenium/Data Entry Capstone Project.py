import requests  # Importing requests to fetch the web page.
from bs4 import BeautifulSoup  # Importing BeautifulSoup for HTML parsing.
import re  # Importing re for regular expressions.
from selenium import webdriver  # Importing Selenium for browser automation.
from selenium.webdriver.common.by import By  # Importing By for locating web elements.
import time  # Importing time to handle delays.

# URL of the Zillow clone website.
clone_url = 'https://appbrewery.github.io/Zillow-Clone/'

# Fetch the web page using requests.
response = requests.get(clone_url)
web_page = response.text  # Get the page content as text.

# Parse the HTML using BeautifulSoup.
soup = BeautifulSoup(web_page, 'html.parser')

# Locate the container holding the listings and extract individual listings.
listings_container = soup.find('ul', class_='List-c11n-8-84-3-photo-cards')
listings = listings_container.find_all('li', class_='ListItem-c11n-8-84-3-StyledListCardWrapper')

# Initialize lists to store links, addresses, and prices for the listings.
link_list = []
address_list = []
price_list = []

# Loop through each listing to extract the required details.
for listing in listings:
    # Extract the link to the listing.
    link_tag = listing.find('a', class_='StyledPropertyCardDataArea-anchor')
    link = link_tag['href'] if link_tag else 'No link available'
    link_list.append(link)

    # Extract the address of the property.
    address_tag = listing.find('address', {'data-test': 'property-card-addr'})
    if address_tag:
        address = address_tag.text.strip()  # Remove leading/trailing spaces.
        address = re.sub(r'\s*\|\s*', ', ', address)  # Replace '|' with a comma for readability.
        address = ' '.join(address.split())  # Normalize whitespace.
    else:
        address = 'No address available'
    address_list.append(address)

    # Extract the price of the property.
    price_tag = listing.find('span', {'data-test': 'property-card-price'})
    if price_tag:
        price = price_tag.text.strip()  # Remove leading/trailing spaces.
        price = re.sub(r'\D', '', price)  # Remove all non-numeric characters.
        price = f"${int(price):,}"  # Format the price with commas.
    else:
        price = 'No price available'
    price_list.append(price)

# Print the extracted data for verification.
print(link_list)
print(address_list)
print(price_list)

# Determine the maximum number of listings to ensure all lists are processed.
max_length = max(len(link_list), len(address_list), len(price_list))

# Set up Chrome WebDriver options to prevent the browser from closing automatically.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver.
driver = webdriver.Chrome(options=chrome_options)

# URL of the Google Form where the data will be submitted.
google_form_url = ''

# Loop through the listings and submit data to the Google Form.
for i in range(max_length):
    # Open the Google Form.
    driver.get(google_form_url)
    time.sleep(10)  # Wait for the form to load.

    # Fill in the address field.
    address_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i1"]')
    address_field.send_keys(address_list[i])

    # Fill in the price field.
    price_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i5"]')
    price_field.send_keys(price_list[i])

    # Fill in the link field.
    link_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i9"]')
    link_field.send_keys(link_list[i])

    # Locate and click the submit button.
    submit_button = driver.find_element(By.XPATH, '//span[@class="NPEfkd RveJvd snByac"]')
    submit_button.click()

    time.sleep(2)  # Wait for the form submission to complete.

# Close the browser after all data has been submitted.
driver.quit()
