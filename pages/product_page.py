from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math
class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
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

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_basket_button.click()

    def should_not_be_presented_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
                "Success message is not presented, but should not be"

    def should_see_as_dissapearing_message(self):
        assert self.is_dissapeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def name_should_match(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CHECK).text, "Wrong name for product"
    def price_should_match(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CHECK).text, "Wrong price for product"