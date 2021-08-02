from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://demo.guru99.com/test/newtours/")

driver.implicitly_wait(10) #wait 10 secs for all element to load
print(driver.title)
assert "Welcome: Mercury Tours" in driver.title

user_element=driver.find_element_by_name("userName")
#print(user_element.is_displayed()) #returns bool
#print(user_element.is_enabled())

password_element=driver.find_element_by_name("password")
#print(password_element.is_displayed()) #returns bool
#print(password_element.is_enabled())
user_element.send_keys("mercury")
password_element.send_keys("mercury")


driver.find_element_by_name("submit").click()
driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a").click()
roundtrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
print('roundtrip button selected: ',roundtrip_radio.is_selected())

oneway_radio=driver.find_element_by_css_selector("input[value=oneway]")
print('oneway button selected: ',oneway_radio.is_selected())
time.sleep(5)
