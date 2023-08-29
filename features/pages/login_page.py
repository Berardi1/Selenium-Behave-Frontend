from features.pages.base_page import BasePage, By


class LoginPage(BasePage):
    # Locators
    login_modal_btn = (By.ID, 'login2')
    username_field = (By.ID, 'loginusername')
    password_field = (By.ID, 'loginpassword')
    login_button = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    welcome_user = (By.ID, 'nameofuser')

    def open_login_modal(self):
        """
        Opens the login modal by clicking on the login modal button.

        This method uses the `find_element` method to locate and click the login modal button.
        """
        self.find_element(self.login_modal_btn).click()

    def get_welcome_text(self):
        """
        Retrieves the welcome text displayed on the page.

        This method waits for the welcome text element to be visible, then retrieves and returns the text.

        Returns:
            str: The welcome text displayed on the page.
        """
        self.wait_visibility_of_element(self.welcome_user)
        return self.find_element(self.welcome_user).text

    def login_credentials(self, credentials: dict):
        """
        Logs in using the provided credentials.

        Args:
            credentials (dict): A dictionary containing the user's login credentials.
        """
        self.find_element(self.username_field).send_keys(credentials['username'])
        self.find_element(self.password_field).send_keys(credentials['password'])
        self.find_element(self.login_button).click()


