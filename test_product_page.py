import time

from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

def test_should_add_to_cart(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    assert browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
        browser.find_element(*ProductPageLocators.PRODUCT_NAME_CHECK).text, "Wrong name for product"
    assert browser.find_element(*ProductPageLocators.PRICE).text == \
        browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CHECK).text, "Wrong price for product"