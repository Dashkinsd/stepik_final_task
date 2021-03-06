from selenium.webdriver.common.by import By
from selenium import webdriver

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in")
    BOOK_TITLE = (By.CSS_SELECTOR, ".col-sm-6.product_main")
    PRICE_VALUE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in")
    PRICE_BOOK = (By.CSS_SELECTOR, "p.price_color")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    BASKET_EMPTY = (By.CSS_SELECTOR, ".content")
    BASKET_PRODUCT = (By.CSS_SELECTOR, ".basket-items")
    ALL_PRODUCTS = (By.CSS_SELECTOR,"[href='/ru/catalogue/']")
    PRODUCT_LINK = (By.CSS_SELECTOR, "[title='Coders at Work']") 
    

