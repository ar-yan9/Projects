from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "your_twitter_email"
TWITTER_PASSWORD = "your_twitter_password"
TWITTER_USERNAME = "your_twitter_username"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(3)

        go_button = self.driver.find_element(By.XPATH, "//a[@class='js-start-btn']")
        go_button.click()
        time.sleep(60)

        self.down = self.driver.find_element(By.XPATH, "//div[@class='result-data download']//span[@class='number result-data-large']").text
        self.up = self.driver.find_element(By.XPATH, "//div[@class='result-data upload']//span[@class='number result-data-large']").text

        print(f"Download: {self.down} Mbps")
        print(f"Upload: {self.up} Mbps")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(3)

        email_field = self.driver.find_element(By.XPATH, "//input[@autocomplete='username']")
        email_field.send_keys(TWITTER_EMAIL)
        email_field.send_keys(Keys.ENTER)
        time.sleep(3)

        try:
            username_field = self.driver.find_element(By.XPATH, "//input[@data-testid='ocfEnterTextTextInput']")
            username_field.send_keys(TWITTER_USERNAME)
            username_field.send_keys(Keys.ENTER)
            time.sleep(3)
        except:
            pass

        password_field = self.driver.find_element(By.XPATH, "//input[@autocomplete='current-password']")
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.ENTER)
        time.sleep(5)

        tweet_box = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0']")
        tweet_box.click()
        tweet_box.send_keys(f"Hey Internet Provider! Why is my internet speed {self.down}Mbps down and {self.up}Mbps up when I am paying for {PROMISED_DOWN}Mbps down and {PROMISED_UP}Mbps up?")
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']")
        tweet_button.click()
        time.sleep(3)
        print("Tweet sent!")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if float(bot.down) < PROMISED_DOWN or float(bot.up) < PROMISED_UP:
    bot.tweet_at_provider()
else:
    print("Internet speed is fine! No tweet sent.")
    