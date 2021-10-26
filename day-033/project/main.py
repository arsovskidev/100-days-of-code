import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 41.00000
MY_LONG = 21.00000


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    print("Checking where is the ISS right now and if it's dark outside...")
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.live.com") as connection:
            connection.starttls()
            connection.login(user="xxx", password="xxx")
            connection.sendmail(
                from_addr="xxx",
                to_addrs="xxx",
                msg="Subject:Look in the sky!\n\nThe ISS is somewhere above you and it's dark so you can see it!",
            )
        print("Emailed successfully!")

    time.sleep(60)
