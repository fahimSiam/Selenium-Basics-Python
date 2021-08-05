#EXPLICIT OR WEBDRIVER WAIT
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
#THESE 2 NEEDED FOR WEBDRIVER WAIT
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://app.hubspot.com/login")

wait=WebDriverWait(driver,10)
#driver.implicitly_wait(10)
wait.until(ec.title_is('HubSpot Login')) #OR USE TITLE_CONTAINS
print(driver.title) #BUT WOULD PRINT CHECKING BROWSER
email_id=wait.until(ec.presence_of_element_located((By.ID,'username'))) #DYNAMIC BUT WILL WAIT !) SECONDS FOR THIS TO LOAD
email_id.send_keys('fahimsiam')
driver.maximize_window()
driver.get("https://app.hubspot.com/login")

#ElementToBeClickable
signup_link=wait.until(ec.element_to_be_clickable(By.LINK_TEXT,'Sign up'))
#ec.presence_of_all_elements_located
#ec.visibility_of_element_located
#ec.frame_to_be_available_and_switch_to_it
#ec.element_to_be_selected
signup_link.click()
