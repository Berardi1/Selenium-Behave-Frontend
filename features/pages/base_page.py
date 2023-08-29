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
        # Set browser with webdriver instance
        self.browser = webdriver
        # Incrementing implicit wait
        self.browser.implicitly_wait(10)

    def wait_alert(self, timeout=10):
        """
        Waits for an alert to be present on the webpage.

        Args:
            timeout (int, optional): The maximum time to wait for the alert to appear, in seconds.
                Defaults to 10 seconds.
        """
        wait = WebDriverWait(self.browser, timeout)
        wait.until(EC.alert_is_present())

    def wait_visibility_of_element(self, locator, timeout=10):
        """
        Waits for an element to become visible on the webpage.

        Args:
            locator: A tuple specifying the locator strategy and value (e.g., (By.ID, 'element_id')).
            timeout (int, optional): The maximum time to wait for the element to become visible, in seconds.
                Defaults to 10 seconds.
        """
        wait = WebDriverWait(self.browser, timeout)
        wait.until(EC.visibility_of_element_located(locator))

    def wait_for_alert_message(self, timeout=10):
        """
        Waits for an alert to be present on the webpage and returns the alert object.

        Args:
            timeout (int, optional): The maximum time to wait for the alert to appear, in seconds.
                Defaults to 10 seconds.

        Returns:
            Alert or False: The alert object if an alert is present, or False if no alert is found.
        """
        wait = WebDriverWait(self.browser, timeout)

        def alert_present(driver):
            try:
                alert = driver.switch_to.alert
                return alert
            except NoAlertPresentException:
                return False

        wait.until(alert_present)

    def get_alert_text(self):
        """
        Gets the text content of an alert.

        Returns:
            str: The text content of the alert.
        """
        self.wait_for_alert_message()
        return Alert(self.browser).text

    def accept_alert(self):
        """
        Accepts the alert present on the webpage.

        This method waits for an alert to appear and then accepts it.

        """
        self.wait_for_alert_message()
        Alert(self.browser).accept()

    def visit_web(self, url):
        """
        Navigates to a specified URL using the WebDriver instance.

        Args:
            url (str): The URL to navigate to.
        """
        self.browser.get(url)

    def find_element(self, locator):
        """
        Finds and returns a web element using the provided locator.

        Args:
            locator (tuple): A tuple specifying the locator strategy and value (e.g., (By.ID, 'element_id')).

        Returns:
            list
        """
        return self.browser.find_element(*locator)



