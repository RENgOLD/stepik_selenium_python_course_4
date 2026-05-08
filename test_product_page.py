import time
import pytest
from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

@pytest.mark.parametrize('link', ["offer0",
                                  "offer1",
                                  "offer2",
                                  "offer3",
                                  "offer4",
                                  "offer5",
                                  "offer6",
                                  pytest.param("offer7", marks=pytest.mark.xfail),
                                  "offer8",
                                  "offer9"
])
def test_guest_can_add_product_to_basket(browser,link):
    #link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    #link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    base_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo='
    page = ProductPage(browser, base_link+link)
    page.open()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product_name_in_message()
    page.should_be_correct_price_in_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart_button()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart_button()
    page.should_disappear()

@pytest.mark.temp
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_should_be_empty()
    page.should_be_empty_cart_text()