import requests
import smtplib
import os
from bs4 import BeautifulSoup


AMAZON_ITEM_URL = os.environ["AMAZON_ITEM_URL"]
USER_AGENT = os.environ["USER_AGENT"]
ACCEPT_LANG = "en-GB,en;q=0.6"
TARGET_PRICE = 400

MY_EMAIL = os.environ["MY_EMAIL"]
MY_APP_PASS = os.environ["MY_APP_PASS"]

# Web Scraping desired Amazon URL for current price of item
headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANG,
}

response = requests.get(url=AMAZON_ITEM_URL, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
item_price = soup.find(name="span", class_="a-offscreen")
item_no_currency = item_price.text.split("$")[1]
item_float_price = float(item_no_currency)

# Emailing user if price is under TARGET_PRICE
if item_float_price <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_APP_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Lego Hogwarts Castle On Sale!!"
                f"\n\nCurrent price: {item_float_price}"
                f"\n\nURL: {AMAZON_ITEM_URL}"
                f"\n\nWill you make the purchase?"
        )
        print("Email has been sent")
else:
    print("Price has not dropped below threshold, no email sent.")
