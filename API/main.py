import requests  # Importing the requests library to handle HTTP requests.
from datetime import datetime  # Importing datetime to work with current time and date.
import smtplib  # Importing smtplib to send email notifications.
import time  # Importing time to introduce delays between iterations.

# Email credentials for sending notifications.
my_email = ""  # Sender's email address.
password = ""  # App-specific password for the sender's email account.

# Your geographic location (latitude and longitude).
MY_LAT = -3.5925  # Replace with your latitude.
MY_LONG = 172.8682  # Replace with your longitude.

# Fetching the current location of the International Space Station (ISS).
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # Raise an exception if the API request fails.
data = response.json()  # Parse the response JSON.

# Extract the ISS's current latitude and longitude.
iss_latitude = float(data["iss_position"]["latitude"])  # ISS's latitude.
iss_longitude = float(data["iss_position"]["longitude"])  # ISS's longitude.

# Check if your position is within ±5 degrees of the ISS's position.
latitude_within_range = abs(MY_LAT - iss_latitude) <= 5
longitude_within_range = abs(MY_LONG - iss_longitude) <= 5

# Parameters for the Sunrise-Sunset API to determine day/night status.
parameters = {
    "lat": MY_LAT,  # Your latitude.
    "lng": MY_LONG,  # Your longitude.
    "formatted": 0,  # Get the time in UTC format.
}

# Fetch sunrise and sunset times for your location.
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()  # Raise an exception if the API request fails.
data = response.json()  # Parse the response JSON.

# Extract the sunrise and sunset times from the API response.
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  # Hour of sunrise (UTC).
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])  # Hour of sunset (UTC).

# Get the current time in hours.
time_now = datetime.now().hour

# Main loop to check conditions periodically.
while True:
    # Pause execution for 60 seconds to avoid excessive API requests.
    time.sleep(60)

    # Check if ISS is overhead and it's nighttime (before sunrise or after sunset).
    if latitude_within_range and longitude_within_range and (time_now >= sunset or time_now <= sunrise):
        # Establish a connection to the Gmail SMTP server.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Secure the connection using TLS.
            connection.login(my_email, password)  # Log in with email credentials.

            # Send an email notification about the ISS being overhead.
            connection.sendmail(
                from_addr=my_email,  # Sender's email address.
                to_addrs="",  # Recipient's email address.
                msg=f"Subject: URGENT - ISS Coming Above !!\n\nLOOK UP"  # Email subject and body.
            )
            connection.close()  # Close the connection to the SMTP server.
