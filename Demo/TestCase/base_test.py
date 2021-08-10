import pathlib
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--start-fullscreen")
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        # self.driver = webdriver.Chrome(executable_path=pathlib.Path(__file__).parent / "../browser/chromedriver", options=options)
        self.driver = webdriver.Chrome(executable_path=pathlib.Path(__file__).parent / "../browser/chromedriver.exe", options=options)
        self.driver.maximize_window()
        # self.driver.set_page_load_timeout(3000)
        # self.driver.get('https://ee-portal.augmedix.com/')
        self.driver.get('https://www.daraz.com.bd/')
        # self.driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        # self.driver.get('https://accounts.google.com/signin/v2/challenge/pwd?flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&navigationDirection=forward&TL=AM3QAYZzdiJaJlzVj3jf_F8SoPrBCfwe0hHPfAMT-b-bMzZ7chiJZhjNIiyFRz9P')

    def tearDown(self):
        self.driver.close()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
