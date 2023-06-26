from selenium import webdriver
from behave import fixture, use_fixture
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.product_store_page import ProductStorePage


@fixture
def selenium_browser_chrome(context):
    context.browser = webdriver.Chrome()
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
    context.base_page = BasePage(context.webdriver)
    context.signup_page = SignupPage(context.webdriver)
    context.cart_page = CartPage(context.webdriver)
    context.login_page = LoginPage(context.webdriver)
    context.product_store_page = ProductStorePage(context.webdriver)
