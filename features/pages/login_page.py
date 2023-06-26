from features.pages.base_page import BasePage, By


class LoginPage(BasePage):
    # Locators
    login_modal = (By.ID, 'login2')
    username = (By.ID, 'loginusername')
    password = (By.ID, 'loginpassword')
    login_button = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
