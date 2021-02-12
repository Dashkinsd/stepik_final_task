from .pages.product_page import ProductPage

#Нажимаем на кнопку Корзины
def test_guest_click_button_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_basket()
    
