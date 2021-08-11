from selenium.webdriver.common.by import By


class SignInPageLocator(object):

    loginOption = (By.XPATH, "//a[contains(text(),'Sign in')]")
    email = (By.XPATH, "//input[@id='j_username']")
    password = (By.XPATH, "//input[@id='j_password']")
    signIn = (By.XPATH, "//button[contains(text(),'Sign In')]")
    invalidAlert = (By.XPATH, "//p[contains(text(),'Wrong email/phone or password')]")
    invalidUser=(By.XPATH,"//body/div[3]/div[1]/p[2]")


