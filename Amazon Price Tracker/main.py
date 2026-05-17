import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/iPhone-Air-256-GB-Promotion/dp/B0FQFTV1NP/"

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "your_app_password"
BUY_PRICE = 100000

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("₹")[1]
price_as_float = float(price_without_currency.replace(",", ""))

print(f"Current Price: ₹{price_as_float}")

if price_as_float < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\nThe price has dropped to ₹{price_as_float}!\nBuy now: {URL}"
        )
        print("Email sent!")
else:
    print(f"Price is still high at ₹{price_as_float}. No email sent.")