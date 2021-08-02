from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.freshworks.com/")

print('THE HEADER IS ',driver.find_element(By.TAG_NAME, 'h1').text)
#IF TAGNAME IS USED THEN .text SHOULD BE THERE
time.sleep(5)
driver.quit()