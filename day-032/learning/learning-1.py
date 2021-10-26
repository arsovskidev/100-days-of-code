import smtplib
import datetime as dt

my_email = "xxx"
my_password = "xxx"

to_email = "xxx"

with smtplib.SMTP("smtp.live.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg="Subject:Hello\n\nThis is the body of my email.",
    )


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2001, month=12, day=8, hour=23)
print(date_of_birth)
