from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def select_choices(drop_list, value):
    try:
        if not value[0]=='all':
            for ele in drop_list:
                print(ele.text)
                for i in range(len(value)):
                    if ele.text == value[i]:
                        ele.click()
                        break
        else:
            for ele in drop_list:
                ele.click()
    except Exception as e:
        print(e)

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(2)

driver.find_element(By.ID,'justAnInputBox').click()

drop_list=driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
value_list= ['choice 3', 'choice 2']
value_list= ['all']
select_choices(drop_list, value_list)
#select_choices(drop_list, 'choice 3')
""" for ele in drop_list:
    print(ele.text)
    if ele.text == 'choice 2 3':
        ele.click()
        break """
