from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.spicejet.com/")
time.sleep(3)

login_ele=driver.find_element(By.ID,'ctl00_HyperLinkLogin')
act_chains=ActionChains(driver)
act_chains.move_to_element(login_ele).perform() #HOVER OVER LOGIN/SIGNUP

SpiceClub_Members_ele=driver.find_element(By.LINK_TEXT,'SpiceClub Members')
act_chains.move_to_element(SpiceClub_Members_ele).perform() #HOVER OVER SPICECLUB MEMBERS

driver.find_element(By.LINK_TEXT,'Member Login').click()









