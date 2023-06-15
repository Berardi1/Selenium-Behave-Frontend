from features.pages.base_page import BasePage, By


class LoginPage(BasePage):
    login_modal = (By.ID, "login2")
    username = (By.ID, "loginusername")
    password = (By.ID, "loginpassword")
