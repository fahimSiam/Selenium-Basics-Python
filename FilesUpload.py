from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

driver.find_element(By.NAME, 'upfile').send_keys('D:\Md Fahim Siam_Resume.pdf')
driver.find_element(By.XPATH,'//input[@type="submit"]').click()