from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://app.hubspot.com/login")
#time.sleep(10)
#driver.find_element(By.LINK_TEXT, 'Get a Free Demo').click()
driver.find_element(By.CLASS_NAME, 'login-email').send_keys('siamfahim02@gmail.com')
#xpath search format: //input[@value='Login']