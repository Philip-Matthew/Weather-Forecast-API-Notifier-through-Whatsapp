import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
OWM_api_key = os.getenv('OWM_API_KEY')
TWO_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
TWO_auth_token = os.getenv('TWILIO_AUTH_TOKEN')

# OWM - Open Weather Map API
# TWO - Twilio

weather_params = {
    "lat": 12.997740,
    "lon": 80.096330,
    "appid": OWM_api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    # For sending an Whatsapp msg
    client = Client(TWO_account_sid, TWO_auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today⛈️. Remember to bring an umbrella☔",
        to='whatsapp:+917604830742'
    )
    print(message.status)
else:
    client = Client(TWO_account_sid, TWO_auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="The weather is clear today☀️😀",
        to='whatsapp:+917604830742'
    )
    print(message.status)
