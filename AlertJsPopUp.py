from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
#time.sleep(3)
