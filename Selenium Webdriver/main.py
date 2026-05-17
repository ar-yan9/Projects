from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Google
driver.get("https://www.google.com")

# Find search bar and search for something
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("Python Selenium")
search_bar.send_keys(Keys.ENTER)

time.sleep(3)

# Get all search results
results = driver.find_elements(By.CSS_SELECTOR, "h3")
for result in results:
    print(result.text)

time.sleep(3)

# Open Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find article count
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(f"Number of articles: {article_count.text}")

time.sleep(3)

driver.quit()
print("Done!")