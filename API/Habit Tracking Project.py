import requests  # Importing requests library for making HTTP requests.
from datetime import datetime  # Importing datetime for working with dates.

# Define user credentials and graph details for the Pixela API.
USERNAME = ""  # Unique username for the Pixela account.
TOKEN = ""  # Authentication token for the Pixela API.
GRAPH_ID = "graph1"  # Identifier for the graph to be created.

# Pixela API base endpoint for user-related actions.
pixela_endpoint = "https://pixe.la/v1/users"

# Parameters for creating a new Pixela user.
user_params = {
    "token": TOKEN,  # Token for API authentication.
    "username": USERNAME,  # Username for the Pixela account.
    "agreeTermsOfService": "yes",  # Agree to the Pixela terms of service.
    "notMinor": "yes"  # Confirm that the user is not a minor.
}

# Uncomment the following lines to create a new Pixela user.
# response = requests.post(url=pixel_endpoint, json=user_params, headers=headers)
# print(response.text)

# Endpoint for creating a graph under the user's account.
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Configuration for creating a new graph.
graph_config = {
    "id": GRAPH_ID,  # Graph ID (must be unique for the user).
    "name": "Cycling Graph",  # Display name for the graph.
    "unit": "Km",  # Unit of measurement (e.g., kilometers for cycling).
    "type": "float",  # Data type of the graph values (e.g., floating point numbers).
    "color": "ajisai"  # Color for the graph (Pixela-specific color codes).
}

# Headers for authentication, including the user token.
headers = {
    "X-USER-TOKEN": TOKEN  # Token used to authenticate API requests.
}

# Uncomment the following lines to create the graph.
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Endpoint for adding values to the graph.
value_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# Define today's date for adding a value to the graph.
today = datetime(year=2024, month=6, day=13)  # Replace with the desired date.

# Configuration for adding a value to the graph.
value_config = {
    "date": today.strftime("%Y%m%d"),  # Format the date as YYYYMMDD.
    "quantity": "15"  # Value to add to the graph (e.g., distance cycled in kilometers).
}

# Uncomment the following lines to add a value to the graph.
# response = requests.post(url=value_endpoint, json=value_config, headers=headers)
# print(response.text)

# Endpoint for updating a specific value in the graph.
update_endpoint = f"{value_endpoint}/{today.strftime('%Y%m%d')}"

# Configuration for updating the value in the graph.
update_endpoint_config = {
    "quantity": "4.5"  # Updated value for the specified date.
}

# Uncomment the following lines to update the value in the graph.
# response = requests.put(url=update_endpoint, json=update_endpoint_config, headers=headers)
# print(response.text)

# Endpoint for deleting a specific value in the graph.
delete_endpoint = f"{update_endpoint}"

# Send a DELETE request to remove the value for the specified date.
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)  # Print the response from the API after deleting the value.
