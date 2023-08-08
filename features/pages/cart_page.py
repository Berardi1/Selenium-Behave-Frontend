from features.pages.base_page import BasePage, By


class CartPage(BasePage):
    # Locators
    open_cart = (By.ID, 'cartur')
    place_order_button = (By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
    order_modal = (By.ID, 'orderModalLabel')
    order_name = (By.ID, 'name')
    order_country = (By.ID, 'country')
    order_city = (By.ID, 'city')
    order_credit_cart = (By.ID, 'card')
    order_month = (By.ID, 'month')
    order_year = (By.ID, 'year')
    purchase_button = (By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')

    def open_cart(self):
        self.find_element(self.open_cart).click()
