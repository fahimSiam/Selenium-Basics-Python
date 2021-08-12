from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common import action_chains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import re
class TestHRM:
    def test_listemployees(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())

        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")


        #clicing the popup cut button
        status=self.driver.find_element(By.XPATH,'//*[@id="divLogo"]/img').is_displayed()
        if(status==True):
            assert True
        else:
            assert False
        self.driver.close()


    

    def test_Login(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())

        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")


        self.driver.find_element(By.ID,'txtUsername').send_keys('siam')
        self.driver.find_element(By.ID,'txtPassword').send_keys('password')
        self.driver.find_element(By.ID,'btnLogin').click()
        act_title=self.driver.title

        if(act_title=="OrangHRM"):
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False