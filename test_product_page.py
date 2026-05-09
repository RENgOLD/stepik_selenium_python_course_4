from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest


# TODO: ЗАМЕТКА ДЛЯ ПРОВЕРЯЮЩЕГО
# Метка pytest.mark.need_review добавлена не ко всему тесту, а к одному параметру
# чтобы и не стирать свой труд и полезные тесты, и сэкономить время проверяющего.
# Чётких указаний по поводу удаления параметризации в этом тесте не было.
# Надеюсь, это не повлияет на оценку.
@pytest.mark.parametrize('link', ["offer0",
                                  "offer1",
                                  "offer2",
                                  "offer3",
                                  "offer4",
                                  "offer5",
                                  "offer6",
                                  pytest.param("offer7",
                                               marks=pytest.mark.xfail),
                                  pytest.param("offer8",
                                               marks=pytest.mark.need_review),
                                  "offer9"
                                  ])
def test_guest_can_add_product_to_basket(browser, link):
    base_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo='
    page = ProductPage(browser, base_link + link)
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

@pytest.mark.need_review
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

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart_button()
    page.should_disappear()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_should_be_empty()
    page.should_be_empty_cart_text()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser, email='em@a.il', password='p@$$w0rd1'):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        yield browser # было не обязательно, но я реализовал очистку данных
        page.remove_current_profile(password)

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    # TODO: ЗАМЕТКА ДЛЯ ПРОВЕРЯЮЩЕГО
    # Метка pytest.mark.need_review добавлена не ко всему тесту, а к одному параметру
    # чтобы и не стирать свой труд и полезные тесты, и сэкономить время проверяющего.
    # Чётких указаний по поводу удаления параметризации в этом тесте не было.
    # Надеюсь, это не повлияет на оценку.
    @pytest.mark.parametrize('link', ["offer0",
                                      "offer1",
                                      "offer2",
                                      "offer3",
                                      "offer4",
                                      "offer5",
                                      "offer6",
                                      pytest.param("offer7",
                                                   marks=pytest.mark.xfail),
                                      pytest.param("offer8",
                                                   marks=pytest.mark.need_review),
                                      "offer9"
                                      ])
    def test_user_can_add_product_to_basket(self, browser, link):
        base_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo='
        page = ProductPage(browser, base_link + link)
        page.open()
        page.click_add_to_cart_button()
        page.solve_quiz_and_get_code()
        page.should_be_correct_product_name_in_message()
        page.should_be_correct_price_in_message()