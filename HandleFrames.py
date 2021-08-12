from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://londonfreelance.org/courses/frames/index.html")
#time.sleep(3)

#driver.switch_to.frame('main') # STARTS FROM 0 IF INDEX OR USE NAME/ID

#ALTERNATE WAY TO FIND FRAME
frame_ele=driver.find_element(By.NAME,'main')
driver.switch_to.frame(frame_ele)
header=driver.find_element(By.CSS_SELECTOR,'body>h2').text
print(header)
driver.switch_to.default_content() #GET BACK TO DEFAULT CONTENT
driver.switch_to.parent_frame() 


driver.quit()

