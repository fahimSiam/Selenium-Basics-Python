from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://expired.badssl.com/")
#time.sleep(3)



print(driver.find_element(By.TAG_NAME,'h1').text)




