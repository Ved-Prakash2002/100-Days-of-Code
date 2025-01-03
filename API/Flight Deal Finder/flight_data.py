from flight_search import FlightSearch  # Import the FlightSearch class for retrieving API tokens.
from datetime import datetime, timedelta  # Import datetime for working with dates and timedelta for date manipulation.
import requests  # Import requests to handle HTTP requests.

# Create an instance of the FlightSearch class to handle API token retrieval.
flightsearch = FlightSearch()


class FlightData:
    """
    A class to interact with the Amadeus API for searching flights and retrieving flight data.
    """

    def __init__(self):
        """
        Initializes the FlightData instance with API endpoints, token, and default date ranges.
        """
        # Endpoint URL for searching flight offers via the Amadeus API.
        self.flight_offers_end_point = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        # Retrieve the access token from the FlightSearch instance.
        self.token = flightsearch.get_token()

        # Set the departure date to tomorrow's date.
        self.departure_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

        # Set the return date to six months from today's date.
        self.arrival_date = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

    def search_flights(self, destination):
        """
        Searches for flights to a given destination using the Amadeus API.

        Parameters:
        - destination: IATA code of the destination city.

        Returns:
        - A JSON object containing flight offers data, or "N/A" if the request fails.
        """
        # Headers for the request, including the authorization token.
        headers = {
            "Authorization": f"Bearer {self.token}"  # Add the access token for authentication.
        }

        # Query parameters for the flight search request.
        params = {
            "originLocationCode": "LON",  # Origin city IATA code (e.g., London).
            "destinationLocationCode": destination,  # Destination city IATA code.
            "departureDate": self.departure_date,  # Departure date.
            "returnDate": self.arrival_date,  # Return date.
            "adults": 1,  # Number of adult passengers.
            "nonStop": "false",  # Allow connecting flights.
            "currencyCode": "GBP"  # Currency for pricing.
        }

        # Send a GET request to the flight offers endpoint with headers and parameters.
        response = requests.get(url=self.flight_offers_end_point, headers=headers, params=params)

        # Handle errors if the response status is not 200 (OK).
        if response.status_code != 200:
            print("Failed to retrieve flight offers:")  # Print error details for debugging.
            print("Status Code:", response.status_code)
            print("Response Body:", response.text)
            print("Request URL:", response.url)
            print("Headers:", headers)
            print("Params:", params)
            return "N/A"  # Return "N/A" if the request fails.

        # Raise an exception for HTTP errors.
        response.raise_for_status()

        # Return the flight data as a JSON object.
        return response.json()

    def find_cheapest_flight(self, flight_data):
        """
        Finds the cheapest flight in the provided flight data.

        Parameters:
        - flight_data: A JSON object containing flight offers data.

        Returns:
        - A dictionary containing the details of the cheapest flight.
        """
        # Handle cases where flight data is missing or invalid.
        if not flight_data or 'data' not in flight_data or not flight_data['data']:
            return {
                "price": "N/A",  # Indicate that no price is available.
                "origin_airport": "N/A",  # Indicate missing origin airport.
                "destination_airport": "N/A",  # Indicate missing destination airport.
                "out_date": "N/A",  # Indicate missing departure date.
                "return_date": "N/A"  # Indicate missing return date.
            }

        # Retrieve the first flight offer (assumed to be the cheapest).
        cheapest_flight = flight_data["data"][0]

        # Extract price and flight route information.
        price = cheapest_flight["price"]["total"]  # Total price of the flight.
        route = cheapest_flight["itineraries"][0]["segments"]  # Flight route segments.

        # Extract departure and return dates.
        out_date = route[0]["departure"]["at"].split("T")[0]  # Departure date (first segment).
        return_date = route[-1]["arrival"]["at"].split("T")[0]  # Return date (last segment).

        # Calculate the number of stopovers and determine the via city.
        stop_overs = len(route) // 2 - 1  # Calculate stopovers based on route length.
        via_city = ""  # Initialize the via city as an empty string.
        if stop_overs > 0:  # If there are stopovers, extract the via city IATA code.
            via_city = route[0]["arrival"]["iataCode"]

        # Construct a dictionary with the flight details.
        flight_details = {
            "price": price,  # Cheapest flight price.
            "origin_airport": route[0]["departure"]["iataCode"],  # Origin airport IATA code.
            "destination_airport": route[-1]["arrival"]["iataCode"],  # Destination airport IATA code.
            "out_date": out_date,  # Departure date.
            "return_date": return_date,  # Return date.
            "stop_overs": stop_overs,  # Number of stopovers.
            "via_city": via_city  # Via city IATA code (if applicable).
        }

        # Return the dictionary containing the flight details.
        return flight_details
