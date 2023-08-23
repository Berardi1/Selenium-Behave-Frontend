from features.pages.base_page import BasePage, By


class SignupPage(BasePage):
    # Locators
    signup_modal = (By.ID, 'signin2')
    username = (By.ID, 'sign-username')
    password = (By.ID, 'sign-password')
    signup_button = (By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')

    def open_signup_modal(self):
        self.find_element(self.signup_modal).click()

    def signup_credentials(self, credentials: dict):
        self.find_element(self.username).send_keys(credentials['username'])
        self.find_element(self.password).send_keys(credentials['password'])
        self.find_element(self.signup_button).click()
