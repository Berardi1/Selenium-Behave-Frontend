from features.pages.base_page import BasePage, By


class ProductStorePage(BasePage):
    products_container = (By.Class, "col-lg-9")
