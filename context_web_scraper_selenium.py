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

def convert_string_nr_to_int(str):
    s = str.replace(',','').replace(' posts', '')
    return float(s.replace('K',''))*1000 if (s.__contains__('K')) else float(s)
    
def reorder_scraping_result(text):
    text = text.split('\n')
    temp = []
    for i in range(0, len(text)):
        if (i+1) % 3 == 0 and i != 0:
            if text[i][0].isdigit() : # and text[i][1].isdigit()
                temp.append((text[i-2], text[i-1], convert_string_nr_to_int(text[i])))
    temp.sort(key=lambda x: x[2], reverse=True)
    return temp

def get_twitter_trends():
    url = 'https://www.twitter.com/i/trends'
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    driver = webdriver.Firefox() # options=options

    driver.get(url)

    username = os.getenv("PESSIMISTIC_USERNAME")
    pw = os.getenv("PESSIMISTIC_PW")

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
    page_content = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div').text
    
    time.sleep(3)
    top_topic = reorder_scraping_result(page_content)[0][1].replace(' ', '%20').replace('#',"%23")
    temp_topic = "Kanye"
    trending_url = f'https://www.twitter.com/search?q="{top_topic}"&src=trend_click&f=live&vertical=trends'
    driver.get(trending_url)

    time.sleep(3)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    trending_content = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div').text

    print(trending_content)

    while True:
        pass

    # driver.quit()
    # return reorder_scraping_result(page_content)

get_twitter_trends()