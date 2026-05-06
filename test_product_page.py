import time

from .pages.product_page import ProductPage
from .pages.main_page import MainPage

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product_name_in_message()
    page.should_be_correct_price_in_message()