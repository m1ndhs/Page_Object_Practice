from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDR_INPUT = (By.ID, "id_registration-email")
    PASSWORD1_INPUT = (By.ID, "id_registration-password1")
    PASSWORD2_INPUT = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
class ProductPageLocators():
    PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_NAME_CHECK = (By.CSS_SELECTOR, "div#messages > div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) strong")
    PRODUCT_PRICE_CHECK = (By.CSS_SELECTOR, "div#messages > .alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
class BasketPageLocators():
    EMPTY_BASKET = (By.ID, "content_inner")
    BASKET_IS_NOT_EMPTY = (By.CLASS_NAME, "basket-title")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[contains(text(), 'View basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")