import requests  # Importing the requests library to handle HTTP requests.

class FlightSearch:
    """
    A class to interact with the Amadeus API for retrieving flight and airport data.
    Handles authentication and fetching IATA codes for cities.
    """

    def __init__(self):
        """
        Initializes the FlightSearch instance with API credentials, endpoints,
        and retrieves an access token for further API interactions.
        """
        self.api_key = "XY1tTCDQ5WDkAGr4G2SK5P57ubc1mIz3"  # API key for the Amadeus API (placeholder).
        self.api_secret = "BB5vDuycK2UBuRO8"  # API secret for the Amadeus API (placeholder).
        self.token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"  # Token generation endpoint.
        self.location_end_point = "https://test.api.amadeus.com/v1/reference-data/locations/cities"  # Endpoint for location data.
        self.token = self.get_new_token()  # Retrieve a new access token during initialization.

    def get_new_token(self):
        """
        Retrieves a new access token from the Amadeus API using the client credentials.

        Returns:
        - The access token as a string.
        """
        # Headers for the token request.
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'  # Specify content type as URL-encoded form data.
        }

        # Body for the token request, including the client credentials.
        body = {
            'grant_type': 'client_credentials',  # OAuth2 grant type.
            'client_id': self.api_key,  # API key.
            'client_secret': self.api_secret  # API secret.
        }

        # Send a POST request to the token endpoint to retrieve the access token.
        response = requests.post(url=self.token_endpoint, headers=header, data=body)

        # Handle errors if the response status is not 200 (OK).
        if response.status_code != 200:
            print("Failed to retrieve token:")  # Print error details for debugging.
            print("Status Code:", response.status_code)
            print("Response Body:", response.text)

        # Raise an exception for HTTP errors.
        response.raise_for_status()

        # Parse the response JSON and extract the access token.
        token_data = response.json()
        return token_data['access_token']  # Return the access token.

    def get_token(self):
        """
        Retrieves the current access token for API authentication.

        Returns:
        - The access token as a string.
        """
        return self.token

    def get_iata_data(self, city):
        """
        Retrieves the IATA code for a given city using the Amadeus API.

        Parameters:
        - city: The name of the city to search for.

        Returns:
        - The IATA code as a string, or "N/A" if not found.
        """
        # Headers for the request, including the authorization token.
        headers = {
            "Authorization": f"Bearer {self.token}"  # Add the access token for authentication.
        }

        # Query parameters for the request.
        params = {
            "keyword": city,  # The city name to search for.
            "max": "2",  # Limit the results to a maximum of 2.
            "include": "AIRPORTS"  # Include only airport data in the response.
        }

        # Send a GET request to the location endpoint with headers and parameters.
        response = requests.get(url=self.location_end_point, headers=headers, params=params)

        # Handle errors if the response status is not 200 (OK).
        if response.status_code != 200:
            print("Failed to retrieve IATA code:")  # Print error details for debugging.
            print("Status Code:", response.status_code)
            print("Response Body:", response.text)
            print("Request URL:", response.url)
            print("Headers:", headers)
            print("Params:", params)

        # Raise an exception for HTTP errors.
        response.raise_for_status()

        # Debugging: Print the response status code and text.
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")

        # Try to extract the IATA code from the response JSON.
        try:
            code = response.json()["data"][0]['iataCode']  # Extract the first IATA code from the response.
        except IndexError:
            # Handle cases where no data is returned for the given city.
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            # Handle cases where the expected key is not found in the response.
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code  # Return the extracted IATA code.
