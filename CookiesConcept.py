from selenium import webdriver
from selenium.webdriver.common import action_chains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import re

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.reddit.com/")

#DOMAIN NAME SHOULD BE SAME AS URL
driver.add_cookie({"name":"fahim","domain":"reddit.com","value":"python"})
"""cookies=driver.get_cookies()

 for cookie in cookies:
    print (cookie) """ #EITHER THIS OR JUST THE ONE LINER
print(driver.get_cookies())
driver.quit()