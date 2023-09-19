from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

url = 'https://www.twitter.com/i/trends'
driver = webdriver.Chrome()
driver.get(url)

mail = "x"
pw = "x"
phone = "x"

email = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
email.click()
email.send_keys(mail)
email.send_keys(Keys.RETURN)

while True:
    pass