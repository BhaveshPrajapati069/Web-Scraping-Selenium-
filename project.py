from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
file = 0

for i in range(1,10):
   driver.get("https://www.amazon.in/s?k=laptop&page={i}&crid=3LEN38FUIZBOU&sprefix=laptop%2Caps%2C268&ref=nb_sb_noss_1")

   elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")
   print(f"{len(elems)} items found")
   for elem in elems:
     d= elem.get_attribute("outerHTML")
     with open(f"data/laptop_{file}.html","w",encoding="utf-8") as f:
         f.write(d)
         file += 1
  # print(elem.text)
  # print(elem.get_attribute("outerHTML"))
   time.sleep(10)
driver.close()