import requests
from datetime import datetime
import time
import smtplib

MY_EMAIL = "smtp.testpersonal2004@gmail.com"
MY_PASS = #truncated
MY_LAT = 25.587215
MY_LNG = 85.122517


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


def is_dark():
    params = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "tzid": "Asia/Kolkata",
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=params,)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


def responder():
    while True:
        try:
            time.sleep(60)  # run every 60 seconds
            if is_iss_overhead() and is_dark():
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASS)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs="shashankbharti899@gmail.com",
                        msg="Subject:Look Up!\n\nISS 🛰️ is Over Your Location!",
                    )
                print("ISS Overhead! Email sent.")
            else:
                print("Not Visible")
        except Exception as e:
            print(f"A problem was encountered: {e}\nRetrying in 60 seconds...")


print("Program has started")
responder()

