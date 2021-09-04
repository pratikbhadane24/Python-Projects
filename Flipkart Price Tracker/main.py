import requests
from bs4 import BeautifulSoup
import smtplib

# Email Sending Google Account Details
MY_EMAIL = "@gmail.com"
PASSWORD = "" 
URL = "" # Product URL
MINI_PRICE = 1000 # Enter minimum price when you want to receive alert

response = requests.get(url=URL)
flip_web_pg = response.text

soup = BeautifulSoup(flip_web_pg, "html.parser")
product = soup.find(name="span", class_="B_NuCI").text
cost = soup.find(name="div", class_="_30jeq3 _16Jk6d").text
final_price = float("".join(d for d in cost if d.isdigit()))
print(final_price)


if final_price < MINI_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        # In to_addrs Enter a Email id where you want the alert.
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="pratikbhadane22@gmail.com",
                            msg=f"Subject: Price Drop\n\n {product} has a price drop please check!")
