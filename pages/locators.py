from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_NAME_CHECK = (By.CSS_SELECTOR, "div#messages > div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) strong")
    PRODUCT_PRICE_CHECK = (By.CSS_SELECTOR, "div#messages > .alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
