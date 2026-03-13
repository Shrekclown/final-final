from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    """Page Object для страницы товара"""
    
    def add_product_to_basket(self):
        """Добавляет товар в корзину"""
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
    
    def get_product_name(self):
        """Возвращает название товара на странице"""
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text
    
    def get_product_price(self):
        """Возвращает цену товара на странице"""
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text
    
    def get_success_message_product_name(self):
        """Возвращает название товара из сообщения об успехе"""
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        return message.text
    
    def get_basket_price_message(self):
        """Возвращает текст сообщения со стоимостью корзины"""
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE)
        return basket_price.text
    
    # === ПОЗИТИВНЫЕ ПРОВЕРКИ ===
    
    def should_be_add_to_basket_button(self):
        """Проверяет наличие кнопки добавления в корзину"""
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Кнопка добавления в корзину не найдена"
    
    def should_be_success_message(self):
        """Проверяет наличие сообщения об успешном добавлении"""
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ELEMENT), \
            "Сообщение об успешном добавлении не появилось"
    
    def should_be_correct_product_name_in_success_message(self, expected_name):
        """Проверяет, что название товара в сообщении совпадает с ожидаемым"""
        actual_name = self.get_success_message_product_name()
        assert actual_name == expected_name, \
            f"Название товара в сообщении '{actual_name}' не совпадает с ожидаемым '{expected_name}'"
    
    def should_be_correct_price_in_basket_message(self, expected_price):
        """Проверяет, что цена в сообщении о стоимости корзины совпадает с ожидаемой"""
        actual_price = self.get_basket_price_message()
        assert actual_price == expected_price, \
            f"Цена в корзине '{actual_price}' не совпадает с ценой товара '{expected_price}'"
    
    # === НЕГАТИВНЫЕ ПРОВЕРКИ ===
    
    def should_not_be_success_message(self, timeout=4):
        """
        Проверяет, что сообщение об успехе НЕ появляется на странице.
        Использует is_not_element_present.
        """
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE_ELEMENT, 
            timeout
        ), "Сообщение об успехе появилось, хотя не должно было"
    
    def should_not_be_success_message_after_addition(self):
        """
        Проверка, что после добавления товара сообщение не появляется.
        Использует is_not_element_present.
        """
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE_ELEMENT, 
            timeout=4
        ), "Сообщение об успехе появилось после добавления товара"
    
    # === ПРОВЕРКИ НА ИСЧЕЗНОВЕНИЕ ===
    
    def success_message_should_disappear(self, timeout=4):
        """
        Проверяет, что сообщение об успехе исчезает со страницы.
        Использует is_disappeared.
        """
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE_ELEMENT, 
            timeout
        ), "Сообщение об успехе не исчезло"