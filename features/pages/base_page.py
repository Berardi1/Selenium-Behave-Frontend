from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    Keys = Keys
    By = By

    def __init__(self, webdriver):
        self.browser = webdriver
        self.browser.implicitly_wait(10)

    def wait_alert(self, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.alert_is_present())

    def wait_visibility_of_element(self, locator, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        wait.until(EC.visibility_of_element_located(locator))

    def accept_alert(self):
        self.wait_alert()
        Alert(self.browser).accept()

    def text_alert(self):
        self.wait_alert()
        return Alert(self.browser).text

    def visit_web(self, url):
        self.browser.get(url)

    def find_element(self, locator):
        return self.browser.find_element(locator)
