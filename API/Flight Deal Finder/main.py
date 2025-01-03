import requests  # Importing requests to handle HTTP requests.
from flight_search import FlightSearch  # Importing the FlightSearch class for flight-related operations.
from data_manager import DataManager  # Importing the DataManager class for handling Google Sheets data.
from flight_data import FlightData  # Importing the FlightData class for flight data operations.
from notification_manager import NotificationManager  # Importing NotificationManager for sending notifications.

# Endpoint URL for accessing the Google Sheets API via Sheety.
end_point = "https://api.sheety.co/c66942d944562f3bc30daf1210de895f/flightDeals/prices"

# Twilio credentials (to be replaced with actual values).
account_sid = ''  # Placeholder for Twilio Account SID.
auth_token = ''  # Placeholder for Twilio Auth Token.

# Initializing instances of the custom classes for different functionalities.
flightsearch = FlightSearch()  # Handles flight search operations.
datamanager = DataManager(end_point)  # Handles Google Sheets data operations.
flightdata = FlightData()  # Manages flight-related data and operations.
notificationmanager = NotificationManager(account_sid, auth_token, from_phone='', to_phone='')  # Manages notifications.

# Fetch data from the Google Sheets endpoint.
response = requests.get(url=end_point)
response.raise_for_status()  # Raise an exception if the request fails.

# Initialize variables to store sheet data and destination IATA codes.
sheet_data = []  # Stores the flight data retrieved from Google Sheets.
destinations = []  # Stores the destination IATA codes.

message = ""  # Placeholder for the notification message.

# Retrieve departure and arrival dates from the flight data.
departure_date = flightdata.departure_date
arrival_date = flightdata.arrival_date

# Extract data from the response JSON and populate `sheet_data`.
for key, value in response.json().items():
    sheet_data = value

# Check and update missing IATA codes in the Google Sheets data.
for item in sheet_data:
    if item['iataCode'] == '':  # If IATA code is missing.
        item['iataCode'] = flightsearch.get_iata_data(item['city'])  # Fetch the IATA code for the city.
        datamanager.update_iota_code(item['id'], item['iataCode'])  # Update the IATA code in the sheet.

# Search for flights for each destination and check for low price alerts.
for item in sheet_data:
    destination = item['iataCode']  # Get the IATA code for the destination.
    print(f"Getting flights for {destination}...")  # Inform about the current destination being processed.

    # Search for flight offers to the destination.
    flight_offers = flightdata.search_flights(destination)

    # Find the cheapest flight from the offers.
    cheapest_flight = flightdata.find_cheapest_flight(flight_offers)

    # If a flight is available, construct the notification message.
    if cheapest_flight['price'] != "N/A":
        message = (
            f"Low price alert! Only GBP {cheapest_flight['price']} to fly from "
            f"{cheapest_flight['origin_airport']} to {cheapest_flight['destination_airport']}, "
            f"from {cheapest_flight['out_date']} to {cheapest_flight['return_date']}."
        )

    # Handle cases where no direct flight is available.
    if cheapest_flight['price'] == "N/A":
        flight_offers = flightdata.search_flights(destination)  # Re-fetch flight offers.
        if flight_offers.get("data"):  # Check if any flight data is available.
            cheapest_flight = flightdata.find_cheapest_flight(flight_offers)  # Get the cheapest flight.
            cheapest_flight['stop_overs'] = 1  # Add a stopover count for indirect flights.
            cheapest_flight['via_city'] = flight_offers["data"][0]["itineraries"][0]["segments"][0]["arrival"][
                "iataCode"]  # Add the city code for the stopover.
            if cheapest_flight.get("stop_overs") > 0:  # If there are stopovers, update the message.
                message += f" Flight has {cheapest_flight['stop_overs']} stopovers"

    # If the flight price is lower than the lowest price in the sheet, send a notification.
    try:
        if float(cheapest_flight['price']) < float(item['lowestPrice']):
            # Uncomment the next line to send an SMS notification.
            # notificationmanager.send_sms(message)
            print(message)  # Print the message to console for testing.
    except ValueError:
        pass  # Handle cases where price data is invalid or missing.

# Send email notifications to all customers.
email_list = datamanager.get_customer_details()  # Retrieve customer email addresses.
for email in email_list:
    notificationmanager.send_emails(email, message)  # Send email with the constructed message.
