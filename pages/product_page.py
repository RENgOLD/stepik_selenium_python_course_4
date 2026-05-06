from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_add_to_cart_button(self):
        add_to_cart_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_correct_product_name_in_message(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, \
            f'Product name "{product_name}" does not match with message "{product_name_in_message}"'

    def should_be_correct_price_in_message(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        cart_value = self.browser.find_element(
            *ProductPageLocators.CART_VALUE).text
        assert product_price == cart_value, \
            f'Product price {product_price} does not match cart value {cart_value}'