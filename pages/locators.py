from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main>h1')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR,
                               'div.alert-success>div.alertinner>strong')
    CART_VALUE = (By.CSS_SELECTOR, 'div.alert-info>div.alertinner>p>strong')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")