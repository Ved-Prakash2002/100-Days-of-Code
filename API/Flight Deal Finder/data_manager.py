import requests  # Importing the requests library to handle HTTP requests.

class DataManager:
    """
    A class responsible for interacting with the external API (Google Sheets via Sheety).
    Handles updating IATA codes and retrieving customer details from the sheet.
    """

    def __init__(self, end_point):
        """
        Initializes the DataManager instance with the provided API endpoint.

        Parameters:
        - end_point: The base URL for the Sheety API used to manage flight price data.
        """
        self.end_point = end_point  # Store the endpoint URL for future use.

    def update_iota_code(self, row_id, iata_code):
        """
        Updates the IATA code for a specific row in the sheet.

        Parameters:
        - row_id: The ID of the row that needs to be updated.
        - iata_code: The new IATA code to be updated in the row.

        Returns:
        - The updated row data returned by the API.
        """
        # Construct the URL for updating the specific row by appending the row ID.
        url = f"{self.end_point}/{row_id}"

        # Create the payload data to update the IATA code.
        iata_data = {
            "price": {
                "iataCode": iata_code  # The new IATA code to be updated.
            }
        }

        # Send the PUT request to update the IATA code for the given row.
        response = requests.put(url=url, json=iata_data)

        # Raise an exception if the API request fails (non-2xx response).
        response.raise_for_status()

        # Return the response data as a Python dictionary.
        return response.json()

    def get_customer_details(self):
        """
        Retrieves the customer details (email addresses) from the Sheety API.

        Returns:
        - A list of email addresses of customers.
        """
        # URL to get customer details from the Sheety API.
        url = "https://api.sheety.co/c66942d944562f3bc30daf1210de895f/flightDeals/users"

        # Send the GET request to retrieve customer data.
        response = requests.get(url=url)

        # Raise an exception if the API request fails (non-2xx response).
        response.raise_for_status()

        # Parse the JSON response to get the customer details.
        data = response.json()

        # Extract and return a list of email addresses from the response data.
        email_list = [item['email'] for (key, value) in data.items() for item in value]

        return email_list  # Return the list of email addresses.
