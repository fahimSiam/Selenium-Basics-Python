import time

from pages.base_page import BasePage
from utils.locators import SignInPageLocator
from testconf.data import logindata


class SignInPage(BasePage):
    def __init__(self, driver):
        self.locator = SignInPageLocator
        super().__init__(driver)

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
        data = self.find_element(*self.locator.invalidAlert).text
        assert data == "Incorrect username or password."

    def test_signin(self):
        self.signIn(logindata.email, logindata.password)
