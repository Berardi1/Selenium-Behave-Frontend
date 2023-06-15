from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    Keys = Keys
    By = By

    def __init__(self, webdriver):
        self.driver = webdriver
        self.wait = WebDriverWait(self.driver,10)
