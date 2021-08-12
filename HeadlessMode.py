from selenium import webdriver
from selenium.webdriver.common import action_chains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import re


#OPTIONS CODE
options=webdriver.ChromeOptions()
#options.headless=True
options.add_argument('--incognito')
driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.reddit.com/")
print(driver.title)