import time
import pytest
from .pages.product_page import ProductPage

@pytest.mark.skip()
def test_should_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.name_should_match()
    page.price_should_match()

# Передаем несколько товаров с промо, фейлящий тест помечаем xfail.
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                 pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.skip()
def test_should_add_to_cart_with_promo(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.name_should_match()
    page.price_should_match()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_presented_succes_message()
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_presented_succes_message()
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(1)
    page.should_see_as_dissapearing_message()