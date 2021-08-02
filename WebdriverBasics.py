from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.google.com/")

driver.find_element(By.NAME,"q").send_keys("flexinja")
#CSS SELECTOR
optionsList =driver.find_elements(By.CSS_SELECTOR, "ul.erkvQe li .wM6W7d span")
print(len(optionsList))

for i in optionsList:
    print(i.text)
    if i.text == 'flexinja crosshair':
        i.click() #CLICKING THE ELEMENT 
        break

time.sleep(2)
driver.quit()