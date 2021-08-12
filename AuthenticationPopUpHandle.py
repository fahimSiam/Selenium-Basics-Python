from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.maximize_window()
#driver.get("https://the-internet.herokuapp.com/basic_auth")
#TO HANDLE POPUP LIKE ROUTER CONFIG PAGES ADD THEM IN THE URL SEPARATED BY :
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
#time.sleep(3)