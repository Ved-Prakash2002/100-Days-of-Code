from selenium import webdriver  # Import Selenium WebDriver for browser automation.
from selenium.webdriver.common.by import By  # Import By for locating web elements.
import time  # Import time for handling delays and tracking elapsed time.

# Configure Chrome WebDriver options to prevent the browser from closing after execution.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the specified options.
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the Cookie Clicker game website.
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Locate the main cookie element to click on.
cookie = driver.find_element(By.ID, value="cookie")

# Locate the element displaying the current cookie count.
cookie_count = driver.find_element(By.ID, value="money")


# Function to retrieve the prices of all available upgrades.
def get_prices():
    """
    Retrieves the prices of store items from the game.

    Returns:
    - A list of tuples containing the web element and its corresponding price.
    """
    elements = driver.find_elements(By.CSS_SELECTOR, "#store b")  # Locate all store item elements.
    prices = []  # List to store the items and their prices.
    for element in elements:
        text = element.text  # Extract the text from the element.
        if '-' in text:  # Check if the element contains a price (formatted as "Item - Price").
            price = int(text.split('-')[1].strip().replace(',', ''))  # Extract and clean the price.
            prices.append((element, price))  # Add the element and price as a tuple to the list.
    return prices  # Return the list of prices.


# Function to retrieve the current cookie count.
def get_cookie_count():
    """
    Retrieves the current number of cookies available.

    Returns:
    - An integer representing the current cookie count.
    """
    count = driver.find_element(By.ID, value="money").text  # Get the text displaying the cookie count.
    if ',' in count:  # Remove commas from the count if present.
        count = count.replace(',', '')
    return int(count)  # Convert the count to an integer and return it.


# Function to purchase the most expensive affordable upgrade.
def upgrades():
    """
    Purchases the most expensive item that the player can currently afford.
    """
    prices = get_prices()  # Retrieve the list of items and their prices.
    cookie_count = get_cookie_count()  # Retrieve the current cookie count.
    # Filter the list to find items that the player can afford.
    affordable_upgrades = [element for element, price in prices if price <= cookie_count]
    if affordable_upgrades:  # If there are affordable items:
        affordable_upgrades[-1].click()  # Click on the most expensive affordable item.


# Main loop to automate clicking and upgrading.
is_true = True  # Flag to control the main loop.
start_time = time.time()  # Record the start time.

while is_true:
    # Simulate clicking the cookie to accumulate points.
    cookie.click()

    # Every 5 seconds, check for upgrades.
    if time.time() - start_time >= 5:
        upgrades()  # Attempt to purchase upgrades.
        start_time = time.time()  # Reset the timer.
