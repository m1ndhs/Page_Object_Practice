from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import math
class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        login_link = self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    #Проверка, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what):

        try:
            WebDriverWait(self.browser, 1).until(EC.presence_of_element_located((how, what)))

        except TimeoutException:
            return True

        return False

#Проверка, что элемент исчезает
    def is_dissapeared(self, how, what, timeout=4):

        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))

        except TimeoutException:
            return False

        return True
    def guest_click_button_to_see_basket(self):
        basket_button = self.browser.find_element(By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a").click()