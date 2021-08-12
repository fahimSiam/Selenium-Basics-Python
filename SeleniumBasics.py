import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver= webdriver.Chrome(ChromeDriverManager().install())
#driver.maximize_window()
driver.get("http://demo.guru99.com/test/newtours/")
print(driver.title)
driver.get("http://demo.automationtesting.in/Windows.html")
time.sleep(2)
#print("Application url is ", driver.current_url)
#print(driver.page_source)
driver.back()
time.sleep(2)
print(driver.title)
driver.forward()
driver.refresh()
time.sleep(2)
print(driver.title)
#driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click() #clicking a button using xpath
#driver.close()#closes focused browser
driver.quit() #closes all windows