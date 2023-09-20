import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()

url = 'https://www.twitter.com/i/trends'
driver = webdriver.Chrome()
driver.get(url)

username = os.getenv("PESSIMISTIC_USERNAME")
pw = os.getenv("PESSIMISTIC_PW")

username_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
username_input.click()
username_input.send_keys(username)
username_input.send_keys(Keys.RETURN)

time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(pw + Keys.RETURN)
actions.perform()

time.sleep(3)
page_content = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div').text

print(page_content)

while True:
    pass