from selenium.webdriver.common.by import By


class SignInPageLocator(object):

    loginOption = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    email = (By.XPATH, '//body/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]')
    password = (By.XPATH, '//body/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]')
    signIn = (By.XPATH, "//button[contains(text(),'LOGIN')]")
    invalidAlert = (By.XPATH, "//div[contains(text(),'Incorrect username or password.')]")


