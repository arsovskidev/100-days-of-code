import os
import smtplib
import datetime as dt
import random


now = dt.datetime.now()

if now.weekday() == 1:
    random_quote = ""
    to_email = "xxx"
    my_email = "xxx"
    my_password = "xxx"

    with open(
        os.path.dirname(os.path.abspath(__file__)) + "/quotes.txt", mode="r"
    ) as file:
        names = file.readlines()
        random_quote = random.choice(names)

    with smtplib.SMTP("smtp.live.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg="Subject:Monday Motivation\n\n" + random_quote,
        )
