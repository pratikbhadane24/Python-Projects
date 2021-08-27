import requests
import smtplib
from requests.api import get

MY_EMAIL = "kadishri@gmail.com"
PASSWORD = "chelsea@7"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "868315BTLYY40G8E"
NEWS_API_KEY = "3b2fc3466bbc4093934a1cbf08177b95"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]
day_before_yesterday_closing_price = data_list[1]["4. close"]

price_difference = abs(float(yesterday_closing_price) -
                       float(day_before_yesterday_closing_price))

diff_percent = (price_difference / float(yesterday_closing_price))*100

if diff_percent > 5:
    news_res = requests.get(url=NEWS_ENDPOINT, params=news_params)

    articles = news_res.json()["articles"]
    three_articles = articles[:3]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=f"pratikbhadane22@gmail.com",
                            msg=f"Subject: Stonkks Alert!👆🏻\n\nThe {STOCK} Stonkks are OUT OF CONTROL!!"
                            )
