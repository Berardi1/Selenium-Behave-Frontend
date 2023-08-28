from features.pages.base_page import BasePage, By


class ProductStorePage(BasePage):
    # Locators
    products_container = (By.ID, "tbodyid")
    add_to_cart = (By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
    product1 = (By.CSS_SELECTOR, '#tbodyid > div:nth-child(1) > div > div > h4 > a')
    product_description = (By.CSS_SELECTOR, '#more-information > strong')

    def open_product(self):
        self.find_element(self.product1).click()

    def add_product_to_cart(self):
        self.find_element(self.add_to_cart).click()

    def get_description(self):
        self.wait_visibility_of_element(self.product_description)
        return self.find_element(self.product_description).text
