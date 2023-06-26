from features.pages.base_page import BasePage, By


class SignupPage(BasePage):
    # Locators
    signup_modal = (By.ID, 'signInModalLabel')
    username = (By.ID, 'sign-username')
    password = (By.ID, 'sign-password')
    signup_button = (By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')

