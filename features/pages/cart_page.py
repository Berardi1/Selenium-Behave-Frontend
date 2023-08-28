from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from features.pages.base_page import BasePage, By


class CartPage(BasePage):
    # Locators
    open_cart_btn = (By.ID, 'cartur')
    delete_btn = (By.CSS_SELECTOR, '#tbodyid > tr > td:nth-child(4) > a')
    product_container = (By.ID, 'tbodyid')
    product_on_cart = (By.CSS_SELECTOR, '#tbodyid > tr > td:nth-child(4) > a')
    place_order_button = (By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
    order_modal = (By.ID, 'orderModalLabel')
    order_name = (By.ID, 'name')
    order_country = (By.ID, 'country')
    order_city = (By.ID, 'city')
    order_credit_card = (By.ID, 'card')
    order_month = (By.ID, 'month')
    order_year = (By.ID, 'year')
    purchase_button = (By.CSS_SELECTOR, '#orderModal > div > div > div.modal-footer > button.btn.btn-primary')
    purchase_message = (By.CSS_SELECTOR, 'body > div.sweet-alert.showSweetAlert.visible > h2')
    product_row = (By.ID, 'page-wrapper')

    def open_cart(self):
        self.find_element(self.open_cart_btn).click()

    def place_order(self):
        self.find_element(self.place_order_button).click()

    def purchase_order(self, credentials: dict):
        self.find_element(self.order_name).send_keys(credentials['name'])
        self.find_element(self.order_country).send_keys(credentials['country'])
        self.find_element(self.order_city).send_keys(credentials['city'])
        self.find_element(self.order_credit_card).send_keys(credentials['credit_card'])
        self.find_element(self.order_month).send_keys(credentials['month'])
        self.find_element(self.order_year).send_keys(credentials['year'])
        self.find_element(self.purchase_button).click()

    def purchase_confirm(self):
        self.wait_visibility_of_element(self.purchase_message)
        return self.find_element(self.purchase_message).text

    def remove_product(self):
        self.find_element(self.delete_btn).click()

    def is_element_not_present(self):
        self.find_element(self.delete_btn).text

