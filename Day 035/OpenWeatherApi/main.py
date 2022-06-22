import requests
from twilio.rest import Client
import os

# get value from env variable
account_sid = os.environ.get("OWN_API_KEY")

# Your Auth Token from twilio.com/console
auth_token  = "*********************"


# https://api.openweathermap.org/data/2.5/onecall?lat=28.7041,
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "**********************"
LAT = 28.7041
LONG = 77.1025
parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid":API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT,params=parameters,verify=False)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12] # sclicing list to 0 to 12

will_rain = False

for hour_data in weather_slice:
    #print(hour_data["weather"])
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    print("It will Rain Today")

client = Client(account_sid, auth_token)

message = client.messages.create(
        to="*****************", 
        from_="*****************",
        body="Hello from Python!")

print(message.sid)
