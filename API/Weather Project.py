import requests  # Importing the requests library for making HTTP requests.
from twilio.rest import Client  # Importing the Twilio client for sending SMS messages.

# OpenWeatherMap API URL for fetching weather forecast data.
url = "https://api.openweathermap.org/data/2.5/forecast"

# Twilio account credentials (to be filled with your actual SID and token).
account_sid = ''  # Twilio Account SID placeholder.
auth_token = ''  # Twilio Auth Token placeholder.

# Parameters for the API request to fetch weather data.
parameters = {
    "lat": 17.431535,  # Latitude of the location to get weather for.
    "lon": 78.500808,  # Longitude of the location to get weather for.
    "appid": "",  # OpenWeatherMap API key placeholder.
    "cnt": 4  # Number of forecast periods to retrieve (e.g., next 4 time slots).
}

# Sending a GET request to the OpenWeatherMap API with the specified parameters.
response = requests.get(url=url, params=parameters)

# Raise an exception if the API request failed (e.g., network issues or invalid API key).
response.raise_for_status()

# Parse the response JSON data into a Python dictionary.
data = response.json()

# Initialize an empty list to store weather condition IDs.
weather_id_list = []

# Iterate through the list of weather forecasts in the API response.
for item in data['list']:
    # Extract the 'weather' dictionary from the current forecast item.
    weather_data = item['weather'][0]

    # Convert the weather data dictionary into a list of (key, value) tuples.
    weather_data_list = [(key, value) for key, value in weather_data.items()]

    # Append the weather condition ID (value of the first key) to the list.
    weather_id_list.append(weather_data_list[0][1])

# Check each weather condition ID in the list.
for weather_id in weather_id_list:
    # If the weather condition ID is less than 700, it indicates bad weather (e.g., rain or snow).
    if int(weather_id) < 700:
        # Create a Twilio client using the account SID and auth token.
        client = Client(account_sid, auth_token)

        # Send an SMS notification about the rain.
        message = client.messages.create(
            body="It's going to rain today. Please carry an umbrella.",  # SMS message body.
            from_='+12562035278',  # Twilio phone number (replace with your Twilio number).
            to='+919150922492'  # Recipient phone number (replace with the intended recipient).
        )

        # Print the status of the sent SMS message.
        print(message.status)
