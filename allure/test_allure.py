from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common import action_chains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import re

@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_title(self):
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


    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip('Skipping this test')
    
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())

        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")


        self.driver.find_element(By.ID,'txtUsername').send_keys('Admin')
        self.driver.find_element(By.ID,'txtPassword').send_keys('admin123')
        self.driver.find_element(By.ID,'btnLogin').click()
        act_title=self.driver.title

        if(act_title=="OrangeHRMe"):
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),
            name="testLoginScreen",
            attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
#allure server D:\files\codes\vs\selenium\allure\reports
# https://app.netlify.com/
# pytest -v -s --alluredir="D:\files\codes\vs\selenium\allure\reports" test_allure.py