import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC


class EnglishPage:
    search_id_locator="searchInput"
    term= "Software"
    wait_time_out=5

    def __init__(self, drv):
        self.drv=drv
        self.wait_variable=W(self.drv,self.wait_time_out)

    
    def search_text(self):
        input_box_element=self.wait_variable.until(EC.presence_of_element_located((By.ID,self.search_id_locator)))
        input_box_element.send_keys(self.term)
        input_box_element.submit()
        self.wait_variable.until(EC.title_contains(self.term))