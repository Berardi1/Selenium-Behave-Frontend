from selenium.common import NoAlertPresentException, NoSuchElementException, TimeoutException
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
        wait = WebDriverWait(self.browser, timeout)
        wait.until(EC.alert_is_present())

    def wait_visibility_of_element(self, locator, timeout=10):
        wait = WebDriverWait(self.browser, timeout)
        wait.until(EC.visibility_of_element_located(locator))

    def wait_for_alert_message(self, timeout=10):
        wait = WebDriverWait(self.browser, timeout)

        def alert_present(driver):
            try:
                alert = driver.switch_to.alert
                return alert
            except NoAlertPresentException:
                return False

        wait.until(alert_present)

    def get_alert_text(self):
        self.wait_for_alert_message()
        return Alert(self.browser).text

    def accept_alert(self):
        self.wait_for_alert_message()
        Alert(self.browser).accept()

    def visit_web(self, url):
        self.browser.get(url)

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def wait_for_element_to_be_removed(self, locator, timeout=5):
        wait = WebDriverWait(self.browser, timeout)
        try:
            wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            pass  # Ignore TimeoutException if element is not removed within timeout

