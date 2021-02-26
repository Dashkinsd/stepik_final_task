from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators

from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Invalid URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
    def register_new_user(self):
        login_or_register = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_or_register.click()
        
        register_email = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        test_email = str(time.time()) + "@yandex.ru"
        register_email.send_keys(test_email) 
        time.sleep(5)
        
        register_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        register_password.send_keys("260220210")
        print("password:"+register_password.text)
     
        
        register_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        register_confirm_password.send_keys("260220210")
        print("password:"+register_confirm_password.text)
       
        
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER)
        register_button.click()
  
        
        
        