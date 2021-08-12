from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")


def select_values(element, value):
    select=Select(element)
    select.select_by_visible_text(value)

    
""" ele_indus=driver.find_element(By.ID, 'Form_submitForm_Industry')
select=Select(ele_indus) #need different names of select
#select.select_by_visible_text('Education')
#select.select_by_index(4)
#select.select_by_value('health')
#print(select.is_multiple) #if not multiple select prints None

#ele_country=driver.find_element(By.ID,'Form_submitForm_Country')
#select_values(ele_indus, 'Education') #function call
#select_values(ele_country, 'Bangladesh')

indus_list=select.options
for ele in indus_list:
    print(ele.text) """


##MAKE XPATH FORMAT //select[@id='Form_submitForm_Industry'] /option

indus_options=driver.find_elements(By.XPATH, "//select[@id='Form_submitForm_Industry'] /option")
print(len(indus_options))
for ele in indus_options:
    print(ele.text)
    if ele.text == 'Education':
        ele.click()
        break



