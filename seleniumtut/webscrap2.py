from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#https://selenium-python.readthedocs.io/waits.html  
import time
path="D:\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://www.techwithtim.net/")

search=driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.ENTER)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main")) 
    )
    articles=main.find_elements_by_tag_name("article")#elements vs element
    for i in articles:
        texts=i.find_element_by_class_name("entry-summary")
        print(texts.text)
finally:
    driver.quit()