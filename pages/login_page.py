#from conftest import browser
from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def register_new_user(self, email, password):
        register_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        register_link.click()

        register_email_textbox = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_TEXTBOX)
        register_email_textbox.send_keys(email)

        register_password1_textbox = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1_TEXTBOX)
        register_password1_textbox.send_keys(password)

        register_password2_textbox = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2_TEXTBOX)
        register_password2_textbox.send_keys(password)

        register_submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        register_submit_button.click()