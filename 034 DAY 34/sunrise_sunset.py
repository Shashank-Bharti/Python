import requests
from datetime import datetime

MY_LAT = 25.587215
MY_LNG = 85.122517

params = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "tzid":"Asia/Kolkata",
    "formatted":0,
    }

response = requests.get("https://api.sunrise-sunset.org/json" , params=params)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
c_hour = (datetime.now()).hour

print(f"{sunrise}\n{sunset}\n{c_hour}")

