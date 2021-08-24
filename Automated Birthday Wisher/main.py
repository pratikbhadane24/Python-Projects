import pandas
import datetime as dt
from random import randint
import smtplib

MY_EMAIL = ""  # Email here (Google)
PASSWORD = ""  # Password

bdays = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
today = (now.month, now.day)

birthdays_dict = {(bdays_row.month, bdays_row.day): bdays_row for (month, bdays_row) in bdays.iterrows()}

if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=f"{birthdays_person.email}",
                            msg=f"Subject: Happy Birthday!\n\n{contents}"
                            )
