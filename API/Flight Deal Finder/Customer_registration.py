import requests  # Importing the requests library to handle HTTP requests.

# Sheety API endpoint for adding new users to the "Flight Deals" club.
sheety_endpoint = "https://api.sheety.co/c66942d944562f3bc30daf1210de895f/flightDeals/users"

# Welcome message for the user, explaining the purpose of the program.
print("Welcome to Ved's Flight Club.\nWe find the best flight deals and email you.")

# Prompt the user to input their first name.
first_name = input("What is your first name?\n")

# Prompt the user to input their last name.
last_name = input("What is your last name?\n")

# Prompt the user to input their email address.
email = input("What is your email?\n")

# Prompt the user to confirm their email address by typing it again.
email_confirm = input("Type your email again.\n")

# Check if the email and confirmation email match.
if email == email_confirm:
    # If the emails match, print a confirmation message to the user.
    print("You're in the club!")

    # Create a dictionary containing the new user's data.
    new_data = {
        "user": {
            "firstName": first_name,  # Add the first name.
            "lastName": last_name,  # Add the last name.
            "email": email  # Add the email address.
        }
    }

    # Send a POST request to the Sheety API to add the new user's data to the database.
    response = requests.post(url=sheety_endpoint, json=new_data)

    # Raise an exception if the API request fails (non-2xx response).
    response.raise_for_status()
