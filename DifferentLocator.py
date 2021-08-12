from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.orangehrm.com/features/hr-administration/")

driver.find_element(By.LINK_TEXT, 'Get a Free Demo').click()

#xpath search format: //input[@value='Login']