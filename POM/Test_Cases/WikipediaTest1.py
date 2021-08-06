import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.EnglishPage import EnglishPage
from Pages.MainPage import MainPage

#import WebPages
driver=webdriver.Chrome(ChromeDriverManager().install())
base_URL='http://www.wikipedia.org'

def set_up():
    driver.get(base_URL)


def test_main_page():
    mp=MainPage(driver)
    mp.test_title()


def test_english_page():
    ep=EnglishPage(driver)
    ep.search_text()


set_up()
test_main_page()
test_english_page()