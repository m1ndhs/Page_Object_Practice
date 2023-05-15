from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    # Ожидаем, что корзина пуста
    def is_basket_empty(self):
        is_element_present = self.is_element_present(*BasketPageLocators.EMPTY_BASKET)
        assert is_element_present, "Your basket is not empty, but should be"

    # Ожидаем, что есть текст о том, что корзина пуста
    def basket_empty_text_is_present(self):
        is_present = self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT)
        assert is_present, "'Empty' text is not present"

    def is_basket_empty_negative(self):
        is_element_not_present = self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET)
        assert is_element_not_present, "Your basket is empty, but should not be"

    def basket_empty_text_is_present_negative(self):
        is_not_present = self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT)
        assert is_not_present, "'Empty' text is present, but should not be"