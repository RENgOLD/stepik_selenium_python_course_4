from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')
    REGISTER_EMAIL_TEXTBOX = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    REGISTER_PASSWORD1_TEXTBOX = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REGISTER_PASSWORD2_TEXTBOX = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main>h1')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR,
                               'div.alert-success>div.alertinner>strong')
    CART_VALUE = (By.CSS_SELECTOR, 'div.alert-info>div.alertinner>p>strong')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_BUTTON = (By.CSS_SELECTOR, 'div.basket-mini>span>a.btn')
    LOGIN_OR_REGISTER_LINK = (By.CSS_SELECTOR, 'a#login_link')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
    PROFILE_DELETE_SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')

class BasketPageLocators:
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, 'div#content_inner>p')
    BASKET_CONTENT = (By.CSS_SELECTOR, 'div#content_inner>div.basket-title')

class ProfilePageLocators:
    DELETE_PROFILE_BUTTON = (By.CSS_SELECTOR, 'a#delete_profile')
    PASSWORD_CONFIRM_TEXTBOX = (By.CSS_SELECTOR, 'input#id_password')
    DELETE_CONFIRM_BUTTON = (By.CSS_SELECTOR, 'button.btn-danger')