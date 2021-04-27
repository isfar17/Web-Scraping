from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
path="D:\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://www.techwithtim.net/")
print(driver.title)
search=driver.find_element_by_name("s")
search.clear()#clearing the text field
search.send_keys("test")
search.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()