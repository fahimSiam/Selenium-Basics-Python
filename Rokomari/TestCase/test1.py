from pages.signin_page import SignInPage
from TestCase.base_test import BaseTest


class TestVerifysignin(BaseTest):

    def test_signin(self):
        page_signin = SignInPage(self.driver)
        page_signin.test_signin()

# python3 -m unittest TestCase.test1
# python3 -m pytest -s TestCase/test1.py --alluredir=ReportAllure &&  allure serve ReportAllure/