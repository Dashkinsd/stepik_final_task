from .pages.product_page import ProductPage
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