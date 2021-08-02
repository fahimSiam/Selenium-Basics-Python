from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
#time.sleep(3)

source=driver.find_element(By.ID, 'draggable')
target=driver.find_element(By.ID, 'droppable')
act_chains=ActionChains(driver)
#act_chains.drag_and_drop(source,target).perform()
#now did this drag&drop with steps like java
act_chains\
    .click_and_hold(source)\
        .move_to_element(target)\
            .release()\
                .perform()




