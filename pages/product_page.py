from .base_page import BasePage
from .locators import ProductPageLocators 
from selenium.webdriver.common.by import By
import time 

#Нажимаем на кнопку Корзины
class ProductPage(BasePage): 
    def click_button_basket(self):
        click_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        click_basket.click()
        #time.sleep(20) 
        BasePage.solve_quiz_and_get_code(self) #Считаем и вводим значение  
        assert self.is_element_present(*ProductPageLocators.BASKET_MESSAGE), "Нет сообщения о добавлении товара в корзину"        
        #time.sleep(120)
        
        product = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE)
        product_text = product.find_element(By.CSS_SELECTOR, " strong")
        print(product_text.text)
        
        book = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        book_text = book.find_element(By.CSS_SELECTOR, " h1")
        print(book_text.text)
        
        assert product_text.text == book_text.text, "Товар не совпадает"
        
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_VALUE)
        price_product_text = price_product.find_element(By.CSS_SELECTOR, " strong")
        print(price_product_text.text)       
        
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        print(price_book.text)
        
        assert price_product_text.text == price_book.text, "Цена не совпадает"
        
        
    #Проверяем сообщение о добавлении товара в корзину



#
#
#
#
#
