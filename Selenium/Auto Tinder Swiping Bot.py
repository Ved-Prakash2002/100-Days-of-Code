from selenium import webdriver  # Import Selenium for web automation.
from selenium.common import NoSuchElementException, ElementClickInterceptedException  # Import exceptions for error handling.
from selenium.webdriver.common.keys import Keys  # Import Keys for keyboard interactions.
from selenium.webdriver.common.by import By  # Import By for locating elements.
import time  # Import time for adding delays.

# Set up Chrome options to keep the browser open after execution.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Prevents the browser from closing automatically.

# Initialize the WebDriver with Chrome options.
driver = webdriver.Chrome(options=chrome_options)

# Open the Tinder website.
driver.get("https://tinder.com/")

# Credentials for Facebook login.
username = ""  # Facebook username or email.
password = ""  # Facebook password.

# Pause to allow the page to load.
time.sleep(2)

# Locate and click the "Log in" button.
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

# Prompt the user to manually click "More Options" and then press ENTER.
input("Click on More Options and Press ENTER")

# Pause to allow the page to load.
time.sleep(2)

# Locate and click the "Log in with Facebook" option.
login_with_facebook = driver.find_element(By.XPATH, '//*[contains(text(),"Log in with Facebook")]')
login_with_facebook.click()

# Switch to the Facebook login popup window.
base_window = driver.window_handles[0]  # Store the main window handle.
fb_login_window = driver.window_handles[1]  # Store the Facebook login window handle.
driver.switch_to.window(fb_login_window)  # Switch to the Facebook login window.
print(driver.title)  # Print the title of the Facebook login window.

# Pause to allow the Facebook login page to load.
time.sleep(2)

# Enter Facebook username and password, then submit the form.
facebook_username = driver.find_element(By.ID, 'email')  # Locate the username field.
facebook_username.send_keys(username)  # Enter the username.

facebook_password = driver.find_element(By.ID, 'pass')  # Locate the password field.
facebook_password.send_keys(password)  # Enter the password.
facebook_password.send_keys(Keys.RETURN)  # Submit the login form.

# Prompt the user to handle any CAPTCHA or additional Facebook prompts manually.
input("Press ENTER")

# Pause to ensure the login process completes.
time.sleep(2)

# Switch back to the main Tinder window.
driver.switch_to.window(base_window)
print(driver.title)  # Print the title of the main Tinder window.

# Pause to allow the Tinder page to load.
time.sleep(5)

# Handle the location permission popup by clicking "Allow."
allow_location_button = driver.find_element(By.XPATH, '//*[text()="Allow"]')
allow_location_button.click()

# Pause to allow the next popup to appear.
time.sleep(2)

# Handle the notifications popup by clicking the "Not Interested" or equivalent button.
notifications_button = driver.find_element(By.CLASS_NAME, 'lxn9zzn')
notifications_button.click()

# Pause before starting the swipe loop.
time.sleep(2)

# Main loop for automated swiping.
while True:
    try:
        # Send the "Right Arrow" key to like a profile.
        body = driver.find_element(By.TAG_NAME, 'body')  # Locate the main body element.
        body.send_keys(Keys.ARROW_RIGHT)  # Simulate a swipe right.
        time.sleep(2)  # Pause before the next swipe.

    except NoSuchElementException:
        # Handle cases where the "Like" button or profile is not found.
        print("Like Button not found.")
        time.sleep(2)  # Pause before retrying.

    except ElementClickInterceptedException:
        # Handle cases where a "Match" popup blocks the swipe.
        try:
            close_match_button = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")  # Locate the close button.
            close_match_button.click()  # Close the match popup.
        except NoSuchElementException:
            # Handle cases where the close button is not found.
            print(" ")
            time.sleep(2)  # Pause before retrying.
