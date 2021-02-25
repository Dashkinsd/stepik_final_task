from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.parametrize('links', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])                                                             
def test_guest_click_button_basket(browser, links): #Нажимаем на кнопку Корзины
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{links}"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_basket()
    print (browser.current_url)

@pytest.mark.parametrize('links', [*range(0,7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_book_title_match(browser, links):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{links}"
    page = ProductPage(browser, link)
    page.open()
    page.book_title_match()
    print (browser.current_url)
    
    
@pytest.mark.parametrize('links', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_price_book_match(browser, links):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{links}"
    page = ProductPage(browser, link)
    page.open()
    page.price_book_match()
    print (browser.current_url)
    
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    print (browser.current_url)
    
def test_guest_cant_see_success_message(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.assert_should_not_be_success_message()
    print (browser.current_url)

@pytest.mark.xfail    
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.explicit_should_not_be_success_message()
    print (browser.current_url) 
    
#гость может перейти на страницу логина со страницы Х    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
гость может перейти на страницу логина со страницы продукта
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.open_product_page()
    page.go_to_basket()

