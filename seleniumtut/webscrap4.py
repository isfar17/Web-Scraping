from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#https://selenium-python.readthedocs.io/waits.html  
import time
path="D:\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_clicker=driver.find_element_by_id("bigCookie")
cookie_count=driver.find_element_by_id("cookies")
driver.implicitly_wait(5)

action=ActionChains(driver)
action.click(cookie_clicker)
while True:
    action.perform()
    ll=[]
    ll.append(driver.find_element_by_id("productPrice4").text)
    ll.append(driver.find_element_by_id("productPrice3").text)
    ll.append(driver.find_element_by_id("productPrice2").text)
    ll.append(driver.find_element_by_id("productPrice1").text)
    ll.sort()
    print(ll)

    
    # item4=driver.find_element_by_id("productPrice4").text
    # item3=driver.find_element_by_id("productPrice3").text
    # item2=driver.find_element_by_id("productPrice2").text
    # item1=driver.find_element_by_id("productPrice1").text
    # item0=driver.find_element_by_id("productPrice0").text
    
