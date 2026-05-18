from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A1%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167187498%2C%22east%22%3A-122.30389832812498%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857114299795826%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%7D"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScASqPf26apjP4XVAMf9j1pDfc6sLL2vLEIfS9tBqf_r6JEDg/viewform"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(ZILLOW_URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_addresses = soup.select(".StyledPropertyCardDataWrapper address")
all_prices = soup.select(".PropertyCardWrapper span")

links = [link["href"] for link in all_link_elements]
addresses = [address.getText().strip().replace("|", "") for address in all_addresses]
prices = [price.getText().strip().split("/")[0] for price in all_prices if "$" in price.getText()]

print(links)
print(addresses)
print(prices)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for i in range(len(addresses)):
    driver.get(GOOGLE_FORM_URL)
    time.sleep(2)

    address_field = driver.find_elements(By.CSS_SELECTOR, ".whsOnd")[0]
    address_field.send_keys(addresses[i])

    price_field = driver.find_elements(By.CSS_SELECTOR, ".whsOnd")[1]
    price_field.send_keys(prices[i])

    link_field = driver.find_elements(By.CSS_SELECTOR, ".whsOnd")[2]
    link_field.send_keys(links[i])

    submit_button = driver.find_element(By.CSS_SELECTOR, ".uArJ5e")
    submit_button.click()
    time.sleep(2)

print("All data entered successfully!")
driver.quit()