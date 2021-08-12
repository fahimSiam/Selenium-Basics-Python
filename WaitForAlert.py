#EXPLICIT OR WEBDRIVER WAIT
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
#THESE 2 NEEDED FOR WEBDRIVER WAIT
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
 
driver.find_element(By.NAME,'proceed').click()

wait=WebDriverWait(driver,10)
alert=wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()
driver.close()
