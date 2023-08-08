from selenium import webdriver
from behave import fixture, use_fixture
from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from features.pages.cart_page import CartPage
from features.pages.signup_page import SignupPage
from features.pages.product_store_page import ProductStorePage


@fixture
def selenium_browser_chrome(context):
    context.webdriver = webdriver.Chrome()
    yield context.webdriver
    context.webdriver.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
    context.base_page = BasePage(context.webdriver)
    context.login_page = LoginPage(context.webdriver)
    context.cart_page = CartPage(context.webdriver)
    context.signup_page = SignupPage(context.webdriver)
    context.product_store_page = ProductStorePage(context.webdriver)

