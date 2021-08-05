from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import  ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.amazon.in/')

best_sellers=driver.find_element(By.LINK_TEXT,'Best Sellers')
#driver.execute_script("arguments[0].click();", best_sellers) #CLICK ELEMENT
title=driver.execute_script("return document.title;") #GET PAGE TITLE
print(title)
#driver.execute_script("history.go(0);") #REFRESHING PAGE SCROPT
#driver.execute_script("alert('hello');")
inner_text=driver.execute_script("return document.documentElement.innerText;")
#print(inner_text) #PRINTING ALL THE TEXTS

driver.execute_script("arguments[0].style.border = '3px solid red'",best_sellers)#GIVING A RED BORDE TO AN ELEMENT
print(driver.execute_script("return navigator.userAgent;")) #USER AGENT INFO 







