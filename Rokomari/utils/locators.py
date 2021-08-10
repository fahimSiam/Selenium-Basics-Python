from selenium.webdriver.common.by import By


class SignInPageLocator(object):

    loginOption = (By.XPATH, "//a[contains(text(),'Sign in')]")
    email = (By.XPATH, "//input[@id='j_username']")
    password = (By.XPATH, "//input[@id='j_password']")
    signIn = (By.XPATH, "//button[contains(text(),'Sign In')]")
    invalidAlert = (By.XPATH, "//div[contains(text(),'Incorrect username or password.')]")


