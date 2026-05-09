from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), \
            'Basket should be empty.'

    def basket_should_be_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_CONTENT), \
            'Basket should be not empty.'

    def should_be_empty_cart_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE), \
            'Should be empty cart message.'

    def should_not_be_empty_cart_text(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE), \
            'Should not be empty cart message.'