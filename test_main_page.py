from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import time 

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)                        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                           # открываем страницу   
    page.go_to_login_page()                               # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()          
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    

def test_guest_can_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    
def test_guest_can_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    
def test_guest_can_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    
    #РАБОТАЕТ ИЗ BasePage! 
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link) #см. Base_Page def __init__
    page.open() # переходим по ссылке
    page.go_to_basket()
    #time.sleep(5)
    #должен обратиться к методу basket_empty_message на странице basket_page
    page.basket_empty_message()
    #time.sleep(5)
    page.basket_without_product()
