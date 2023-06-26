from features.pages.base_page import BasePage, By


class ProductStorePage(BasePage):
    # Locators
    products_container = (By.ID, "tbodyid")
