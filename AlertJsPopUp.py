from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
#time.sleep(3)


driver.find_element(By.NAME, 'proceed').click()
time.sleep(3)


alert=driver.switch_to.alert #HANDLING ALERT POPUP
print(alert.text)
alert.accept() #accept popup
#alert.dismiss() #cancel popup
#alert.send_keys('hi')
driver.switch_to.default_content() #return to webpage



