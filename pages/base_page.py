from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
import pytest 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
#from .basket_page import BasketPage
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, browser, url, timeout=10): #конструктор, сюда передаются значения из page = MainPage(browser, link)
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)
    
    def open(self): #должен открывать нужную страницу в браузере, используя метод get()
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID) #добавили в уроке 4.3 шаг 8
        link.click()

    def click_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK) #добавили в уроке 4.3 шаг 8
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
        
       
    def solve_quiz_and_get_code(self):   #Считаем код
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    # проверяет, что элемент не появляется на странице в течение заданного времени
    # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

#будет ждать до тех пор, пока элемент не исчезнет
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
        
     #переходим на страницу корзины   
    #def go_to_basket(self):
        #link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        #link.click()
        
    #def basket_empty_message(self):
        #basket = self.browser.find_element(*BasePageLocators.BASKET_EMPTY)
        #basket_text = basket.find_element(By.CSS_SELECTOR, " div p") 
        #print(basket_text.text)
        #assert basket_text.text == "Ваша корзина пуста Продолжить покупки", "Нет сообщения о пустой корзине"
        
        
        