import time

from .pages.product_page import ProductPage
from .pages.main_page import MainPage

def test_add_to_cart_with_quiz(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()