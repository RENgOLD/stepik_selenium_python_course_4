from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_add_to_cart_button(self):
        add_to_cart_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
