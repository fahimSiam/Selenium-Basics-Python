import time

from pages.base_page import BasePage
from utils.locators import SignInPageLocator
from testconf.data import logindata
from selenium.common.exceptions import NoSuchElementException

class SignInPage(BasePage):
    def __init__(self, driver, testCase):
        self.locator = SignInPageLocator
        self.testCase=testCase
        super().__init__(driver,testCase)

    def click_on_login_option(self):
        self.find_element(*self.locator.loginOption).click()

    def signIn(self, email, password):
        self.click_on_login_option()
        time.sleep(5)
        self.find_element(*self.locator.email).send_keys(email)
        time.sleep(5)
        self.find_element(*self.locator.password).send_keys(password)
        time.sleep(5)
        self.find_element(*self.locator.signIn).click()
        time.sleep(2)
        try:
            data = self.find_element(*self.locator.invalidAlert).text
            #invalidEmailData=self.find_element(*self.locator.invalidUser).text
            print('error meesage is: '+data)
            #print('Invalid email is '+invalidEmailData )
            assert data == "Wrong email/phone or password"
               
               # print('Invalid email is ',invalidEmailData )
        except NoSuchElementException:
            print('login success if no invalid message printed')
        try:
            invalidEmailData=self.find_element(*self.locator.invalidUser).text
            print('Invalid email is message: '+invalidEmailData )
            assert invalidEmailData == "Wrong email or phone "+email
        except NoSuchElementException:
            print('login success if no invalid message printed')
    def test_signin(self, testCase):
        self.testCase=testCase
        loginData=logindata()
        email,password=loginData.getLoginData(testCase)
        self.signIn(email, password)
