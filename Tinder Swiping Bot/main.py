from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://tinder.com")
time.sleep(2)

# Login with Google
login_button = driver.find_element(By.XPATH, '//*[@id="o-1175990514"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
time.sleep(2)

google_login = driver.find_element(By.XPATH, '//*[@id="o-1175990514"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/span/div[2]/button')
google_login.click()
time.sleep(5)

# Switch to Google login window
base_window = driver.window_handles[0]
google_window = driver.window_handles[1]
driver.switch_to.window(google_window)

email_field = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_field.send_keys("your_google_email")

next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next_button.click()
time.sleep(3)

password_field = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_field.send_keys("your_google_password")

next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
next_button.click()
time.sleep(5)

driver.switch_to.window(base_window)
time.sleep(5)

# Handle popups
try:
    allow_location = driver.find_element(By.XPATH, "//button[contains(text(),'Allow')]")
    allow_location.click()
except:
    pass

try:
    deny_notification = driver.find_element(By.XPATH, "//button[contains(text(),'Not interested')]")
    deny_notification.click()
except:
    pass

time.sleep(2)

# Start swiping
for _ in range(100):
    time.sleep(1)
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="o-1175990514"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except NoSuchElementException:
        pass
    except ElementClickInterceptedException:
        try:
            close_button = driver.find_element(By.XPATH, '//*[@id="o-1175990514"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div/div/div[3]/button[2]')
            close_button.click()
        except:
            pass