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

def get_analysis_of_tweet(behavior, tweet_id):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options) 

    behavior = behavior.upper()

    username = os.getenv(f"{behavior}_USERNAME")
    pw = os.getenv(f"{behavior}_PW")

    driver.get('https://www.twitter.com/i/trends')

    time.sleep(3)
    username_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
    username_input.click()
    username_input.send_keys(username)
    username_input.send_keys(Keys.RETURN)

    time.sleep(3)
    actions = ActionChains(driver)
    actions.send_keys(pw + Keys.RETURN)
    actions.perform()
    
    time.sleep(3)
    url = f'https://www.twitter.com/{username}/status/{tweet_id}/analytics'

    print(username + " " + pw)

    driver.get(url)
    time.sleep(3)

    if driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/span").text == "Something went wrong":
        return "0", "0", "0", "0", "0", "0", "0", "0"

    likes = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div/span").text
    retweets = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/span").text
    comments = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div/div[3]/div/span").text
    impressions = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/span/div/span").text
    engagements = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/span/div/span").text
    detail_expands = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/span/div/span").text
    new_followers = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[2]/div/span/div/span").text
    profile_visits = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/div/span/div/span").text

    return likes, retweets, comments, impressions, engagements, detail_expands, new_followers, profile_visits
