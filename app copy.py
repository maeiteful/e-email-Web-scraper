from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
import csv
import time
import pandas as pd
import math   


courses = []
chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument('--disable-gpu')
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.get("https://www.tradingcup.com/en/rank/mmr")
time.sleep(3)
dictionary = {}
t=1
counter=1


while counter != 1747:
    try:
        if driver.find_element("xpath", '//*[@id="root"]/main/section/div/div[3]/table/tbody/tr[{}]'.format(t)):
            time.sleep(0.1)
            driver.find_element("xpath",'//*[@id="root"]/main/section/div/div[3]/table/tbody/tr[{}]'.format(t)).click()
            string = driver.current_url
            stringF= string.replace("https://www.tradingcup.com/en/", "")
            driver.get("https://proddata.tradingcup.com/"+ stringF +"/basic")
            time.sleep(0.5)
            string2 = driver.find_element("xpath",'/html/body/pre').text
            data = json.loads(string2)
            try:
                dictionary[counter] = data['data']
                print(dictionary[counter])
                print()
                print(counter)
            except:
                print("No Data")
                print(counter)
    except:
        print("number skipped")
    
    t= t+1
    counter= counter+1
    if t == 21:
        t=1
    page = int((counter-1)/20)
    print (page)
    driver.get("https://www.tradingcup.com/en/rank/mmr")
    time.sleep(1.5)
    try:
        if page > 0:
            for i in range(page):
                driver.find_element("xpath",'//*[@id="root"]/main/section/div/div[4]/div[2]/button[3]').click()
                time.sleep(0.01)
    except:
        print("error")
    time.sleep(1.2)
    #driver.find_element("xpath",'//*[@id="root"]/main/section/div/div[4]/div[2]/button[3]').click()


df = pd.DataFrame.from_dict(dictionary, orient='index') 
df.to_csv (r'test10.csv', index=False, header=True)