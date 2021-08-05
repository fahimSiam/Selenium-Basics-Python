from selenium import webdriver
from selenium.webdriver.common import action_chains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import re


#OPTIONS CODE
options=webdriver.ChromeOptions()
options.headless=True
driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.reddit.com/")
#driver.get_screenshot_as_file('reddit.png')

'''FULL BODY SCREENSHOT'''
#HAVE TO RUN HEADLESS MODE TO TAKE FULL SS
S=lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('reddit_fullpage.png')

driver.quit()