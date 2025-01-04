import requests  # Importing the requests library for making HTTP requests.
from twilio.rest import Client  # Importing Twilio client for sending SMS messages.

# Constants for stock and company details.
STOCK_NAME = "TSLA"  # Stock ticker symbol for Tesla.
COMPANY_NAME = "Tesla Inc"  # Full name of the company.

# API endpoints for stock data and news data.
STOCK_ENDPOINT = "https://www.alphavantage.co/query"  # Alpha Vantage API endpoint.
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"  # News API endpoint.

# Twilio credentials for SMS notifications.
account_sid = ''  # Twilio account SID.
auth_token = ''  # Twilio authentication token.

# Parameters for fetching stock data from the Alpha Vantage API.
stock_parameters = {
    "function": "TIME_SERIES_DAILY",  # API function to get daily time series stock data.
    "symbol": STOCK_NAME,  # The stock ticker symbol to query.
    "apikey": "ECW5JK7KGQOMNVZY"  # API key for authentication.
}

# Parameters for fetching news data from the News API.
news_parameters = {
    'q': 'Tesla&',  # Query keyword for the company name.
    'from': '2024-06-12&',  # Start date for news articles.
    'sortBy': 'popularity&',  # Sort articles by popularity.
    'apiKey': 'cc6bdad26f704984aeb0d960d190d200'  # API key for authentication.
}

# Fetch stock data from the Alpha Vantage API.
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()  # Raise an exception if the request fails.
stock_data = stock_response.json()  # Parse the response JSON.

# Fetch news data from the News API.
news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()  # Raise an exception if the request fails.
news_data = news_response.json()  # Parse the response JSON.

# Simulated closing prices for testing (replace with API data when available).
closing_prices = [182, 173]  # Replace this with parsed stock data from the API.

# Extract the closing prices for yesterday and the day before yesterday.
# Uncomment the following line to use real data from the API:
# closing_prices = [float(value["4. close"]) for (key, value) in stock_data['Time Series (Daily)'].items()]
yesterday_closing_price = closing_prices[0]  # Closing price for yesterday.
day_before_yesterday_closing_price = closing_prices[1]  # Closing price for the day before yesterday.

# Calculate the absolute and percentage difference in closing prices.
positive_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
percentage_difference = (positive_difference / day_before_yesterday_closing_price) * 100

# Initialize a list to store formatted news articles.
formatted_articles = []

# Check if the percentage difference exceeds 5%.
if percentage_difference > 5:
    # Extract the top three news articles about Tesla.
    tesla_news_data = [value for (key, value) in news_data.items()]
    tesla_news_list = tesla_news_data[2]  # List of news articles.

    # Format the top three news articles for SMS notifications.
    for i in range(3):
        title = tesla_news_list[i]['title']  # Article title.
        description = tesla_news_list[i]['description']  # Article description.
        message_body = (f"{STOCK_NAME}: increase 5%\n"  # Construct the message body.
                        f"Headline: {title}\n"
                        f"Brief: {description}\n")
        formatted_articles.append(message_body)  # Add the formatted message to the list.
else:
    # Print a message if the percentage difference is not significant.
    print("Nothing")

# Initialize the Twilio client for sending SMS notifications.
client = Client(account_sid, auth_token)

# Send each formatted article as an SMS message.
for article in formatted_articles:
    message = client.messages.create(
            body=article,  # SMS message body.
            from_='',  # Twilio phone number (sender).
            to=''  # Recipient's phone number.
        )
    print(f"Sent message {article}")  # Print confirmation for each sent message.
