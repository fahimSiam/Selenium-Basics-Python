from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com/")

#driver.find_element_by_xpath("//*[@id='wizardMainRegionV2']/div/div/div[2]/div/div/ul/li[2]/a/span").click()
driver.find_element(By.XPATH,'//*[@id="wizardMainRegionV2"]/div/div/div[2]/div/div/ul/li[2]/a/span').click() #going to flight page
#location from click chropath
driver.find_element(By.XPATH, "//body/div[@id='app']/div[@id='app-layer-manager']/div[@id='app-layer-base']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
driver.find_element(By.XPATH, "//input[@id='location-field-leg1-origin']").send_keys("SFO") #location from input

#location to click chropath
driver.find_element(By.XPATH, "//body/div[@id='app']/div[@id='app-layer-manager']/div[@id='app-layer-base']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
#driver.find_element(By.XPATH, "//body/div[@id='app']/div[@id='app-layer-manager']/div[@id='app-layer-location-field-leg1-destination-ta-dialog']/div[2]/div[1]/div[1]/section[1]/div[1]/input[1]").send_keys("NYC") #location to input

