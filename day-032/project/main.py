import os
import pandas
import datetime as dt
import random
import smtplib

EMAIL = "xxx"
PASSWORD = "xxx"

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
NOW = dt.datetime.now()

LETTER_TEMPLATES = [
    "letter_1.txt",
    "letter_2.txt",
    "letter_3.txt",
]

# Reading the CSV for the birth dates.
birthdays = pandas.read_csv(DIRECTORY + "/birthdays.csv")
birthdays_filtered = birthdays[
    (birthdays["month"] == NOW.month) & (birthdays["day"] == NOW.day)
].to_dict(orient="records")

# Sending email function.
def send_mail(email, name, year):
    with open(
        DIRECTORY + "/letter_templates/" + random.choice(LETTER_TEMPLATES), mode="r"
    ) as file:
        letter = file.read()

    letter = letter.replace("[NAME]", name)
    letter = letter.replace("[AGE]", str(NOW.year - year))

    with smtplib.SMTP("smtp.live.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=email,
            msg="Subject:Happy Birthday!\n\n" + letter,
        )


# Checking if there are any birthdays today.
if birthdays_filtered:
    for person in birthdays_filtered:
        send_mail(person["email"], person["name"], person["year"])
else:
    print("There are no birthdays for today, check tomorrow!")
