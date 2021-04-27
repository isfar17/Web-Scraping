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

text=driver.find_element_by_link_text("Game Development With Python")
text.click()
try:
    linktext = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "General Pygame Tutorial")) 
    )
    linktext.click()
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003")) 
    )
    link.click()
    driver.back()
    driver.back()
    driver.back()

except:
    driver.quit()
