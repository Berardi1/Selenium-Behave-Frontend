from features.pages.base_page import BasePage, By


class ProductStorePage(BasePage):
    # Locators
    products_container = (By.ID, "tbodyid")
    add_to_cart = (By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')

    def add_product_to_cart(self):
        self.find_element(self.add_to_cart).click()

