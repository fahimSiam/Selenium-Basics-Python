from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.amazon.in/")

linksList = driver.find_elements(By.TAG_NAME, 'a')
print(len(linksList))

imgList = driver.find_elements(By.TAG_NAME, 'img')
print(len(imgList))

#or ele in linksList:
   # print(ele.text)
   #print(ele.get_attribute('href'))
for ele in imgList:
    print(ele.get_attribute('src'))
