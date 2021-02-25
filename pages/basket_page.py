from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators 
from .locators import BasketPageLocators
import time 


class BasketPage(BasePage): 
        
    def go_to_basket(self):
        link_basket = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link_basket.click()
        
        #в корзине нет товаров
        #assert 
       
    def basket_empty_message(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)
        basket_text = basket.find_element(By.CSS_SELECTOR, " div p") 
        #print(basket_text.text)
        assert basket_text.text == "Ваша корзина пуста Продолжить покупки", "Нет сообщения о пустой корзине"
        
    def basket_without_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
       "Product is presented, but should not be"
    
    def open_product_page(self):
        link_all_products = self.browser.find_element(*BasketPageLocators.ALL_PRODUCTS)
        link_all_products.click()
        link_go_to_product = self.browser.find_element(*BasketPageLocators.PRODUCT_LINK)
        link_go_to_product.click()