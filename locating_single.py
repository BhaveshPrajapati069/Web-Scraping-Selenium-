from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get("https://www.amazon.in/s?k=laptop&crid=3LEN38FUIZBOU&sprefix=laptop%2Caps%2C268&ref=nb_sb_noss_1")

elem = driver.find_element(By.CLASS_NAME,"puis-card-container")
print(elem.get_attribute("outerHTML"))
time.sleep(10)
driver.close()