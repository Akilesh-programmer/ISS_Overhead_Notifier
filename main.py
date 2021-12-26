import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "akileshpython@gmail.com"
MY_PASSWORD = "Thilagu@123"

MY_LAT = 11.341036
MY_LONG = 77.717163

go_on = True

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_close():
    lat_close = False
    lng_close = False
    if 6.341036 <= iss_latitude <= 16.341036:
        lat_close = True
    if 72.717163 <= iss_longitude <= 82.717163:
        lng_close = True
    if lat_close and lng_close:
        return True
    else:
        return False


def is_dark():
    time_now = datetime.now()
    time_now = str(time_now)
    time_now = time_now.split(" ")[1].split(":")[0]
    print(time_now)
    if int(time_now) == 18 or int(time_now) == 19 or int(time_now) == 20 or int(time_now) == 21 or int(
            time_now) == 22 or int(time_now) == 23 or int(time_now) == 0 or int(time_now) == 1 or int(
            time_now) == 2 or int(time_now) == 3 or int(time_now) == 4 or int(time_now) == 5 or int(time_now) == 6:
        return True
    else:
        return False


def send_mail():
    if is_close():
        print("yes")
        if is_dark():
            print("yes")
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="akileshakileshs1234@gmail.com",
                                msg="Subject:ISS is near.\n\n The International Space Station is closer to you. Go and "
                                    "look in the sky"
                                )
            connection.close()


while go_on:
    send_mail()
    time.sleep(60)
