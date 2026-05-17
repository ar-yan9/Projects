 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "your_linkedin_email"
PASSWORD = "your_linkedin_password"
PHONE = "your_phone_number"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.linkedin.com/login")
time.sleep(2)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(EMAIL)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(3)

driver.get("https://www.linkedin.com/jobs/search/?keywords=Python%20Developer&location=India&f_AL=true")
time.sleep(3)

jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in jobs:
    try:
        job.click()
        time.sleep(2)

        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        apply_button.click()
        time.sleep(2)

        try:
            phone_field = driver.find_element(By.CSS_SELECTOR, "input[id*='phoneNumber']")
            phone_field.clear()
            phone_field.send_keys(PHONE)
        except:
            pass

        try:
            submit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']")
            submit_button.click()
            print("Application submitted!")
        except:
            print("Application needs more info - skipping")
            close_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss']")
            close_button.click()

    except Exception as e:
        print(f"Could not apply: {e}")

driver.quit()