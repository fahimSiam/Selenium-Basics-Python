from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
#time.sleep(3)

#RIGHT/CONTEXT CLICK EXAMPLE 
right_click_ele= driver.find_element(By.XPATH,"//span[contains(text(),'right click me')]")
act_chain=ActionChains(driver) 
act_chain.context_click(right_click_ele).perform()

menu_list=driver.find_elements(By.CSS_SELECTOR,'li.context-menu-icon span')

for i in menu_list:
    print(i.text)
#act_chain.send_keys_to_element(element, value).perform()
#act_chain.click().perform()
act_chain.double_click()
time.sleep(3)
driver.quit()