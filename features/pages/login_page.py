from features.pages.base_page import BasePage, By


class LoginPage(BasePage):
    # Locators
    login_modal = (By.ID, 'login2')
    username_field = (By.ID, 'loginusername')
    password_field = (By.ID, 'loginpassword')
    login_button = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    welcome_user = (By.ID, 'nameofuser')

    def open_login_modal(self):
        self.find_element(self.login_modal).click()

    def get_welcome(self):
        self.wait_visibility_of_element('nameofuser')
        return self.find_element(self.welcome_user).text

    def login_credentials(self, credentials: dict):
        self.find_element(self.username_field).send_keys(credentials['username'])
        self.find_element(self.password_field).send_keys(credentials['password'])
        self.find_element(self.login_modal,self.login_button).click()

