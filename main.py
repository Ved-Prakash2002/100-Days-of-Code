import requests
from twilio.rest import Client

url = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = ''
auth_token = ''

parameters = {
    "lat": 17.431535,
    "lon": 78.500808,
    "appid": "",
    "cnt": 4
}

response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()

weather_id_list = []

for item in data['list']:
    weather_data = item['weather'][0]

    weather_data_list = [(key, value) for key, value in weather_data.items()]
    weather_id_list.append(weather_data_list[0][1])

for weather_id in weather_id_list:
    if int(weather_id) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Please carry an umbrella.",
            from_='+12562035278',
            to='+919150922492'
        )
        print(message.status)
