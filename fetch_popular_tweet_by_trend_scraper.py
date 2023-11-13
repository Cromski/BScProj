import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
from selenium.webdriver.common.action_chains import ActionChains
import re
# import _tkinter

load_dotenv()

def convert_string_nr_to_int(str):
    s = str.replace(',','').replace(' posts', '')
    return float(s.replace('K',''))*1000 if (s.__contains__('K')) else float(s.replace('M',''))*1000000 if (s.__contains__('M')) else float(s)

def reorder_scraping_result(text):
    pattern = r'^\d+\n·'
    text = re.split(pattern, text, flags=re.MULTILINE)
    text = [segment.strip() for segment in text if segment.strip()]
    for i in range(0, len(text)):
        short_data = text[i].split('\n')
        if len(short_data) == 3:
            if short_data[2].__contains__('posts'):
                text[i] = (short_data[0], short_data[1], convert_string_nr_to_int(short_data[2]))
            else:
                text[i] = (short_data[0], short_data[1], 0.0)
        else:
            text[i] = (short_data[0], short_data[1], 0.0)

    return sorted(text, key=lambda x: float(x[-1]), reverse=True)


def get_twitter_trends():
    url = 'https://www.twitter.com/i/trends'
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    driver = webdriver.Firefox() # options=options

    driver.get(url)

    username = os.getenv("PESSIMISTIC_USERNAME")
    pw = os.getenv("PESSIMISTIC_PW")

    time.sleep(3)
    username_input = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
    username_input.click()
    username_input.send_keys(username)
    username_input.send_keys(Keys.RETURN)

    time.sleep(3)
    actions = ActionChains(driver)
    actions.send_keys(pw + Keys.RETURN)
    actions.perform()

    time.sleep(3)
    page_content = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div'))).text
    
    time.sleep(3)
    trend = reorder_scraping_result(page_content)[0][1]
    fixed_trend = trend.replace('#', '%23') if trend[0] == '#' else trend

    trending_url = f'https://twitter.com/search?q=%22{fixed_trend}%22%20filter%3Aimages&src=typed_query&f=media'
    driver.get(trending_url)

    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[2]'))).click()
    top_tweet_text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[1]/div'))).text
    top_tweet_div = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[2]/div/div")))

    click_tweet = webdriver.common.action_chains.ActionChains(driver)
    click_tweet.move_to_element_with_offset(top_tweet_div, 0, -5).click().perform()

    top_tweet_attachment = driver.find_elements(By.TAG_NAME, "img") # gets all images on the page
    # gets the first image
    tweet_src = ""
    for attachment in top_tweet_attachment:
        if attachment.get_attribute("src").__contains__("/media/"):
            tweet_src = attachment.get_attribute("src")
            break

    # print(f'top tweet text: {top_tweet_text}\nTop tweet src: {tweet_src} bingo')

    driver.quit()
    return top_tweet_text, tweet_src

# bing,bong = get_twitter_trends()
# print(f'bing: {bing}\nbong: {bong}')