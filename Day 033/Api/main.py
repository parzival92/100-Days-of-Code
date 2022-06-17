import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude =data["iss_position"]["latitude"]
# iss_pos = (longitude,latitude)
# print(iss_pos)


MY_LAT = "27.476219"
MY_LONG = "77.693398"

paramters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted":0,
}

# Use SSL verify false for ssl error
response = requests.get(url="https://api.sunrise-sunset.org/json",params=paramters,verify=False)

response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()
print(time_now.hour)
print(sunrise)
print(sunset)

