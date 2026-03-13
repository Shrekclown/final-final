import pytest
from pages.product_page import ProductPage

class TestProductPage:
    """Тесты для страницы товара"""
    
    @pytest.mark.xfail(reason="Сообщение появляется сразу после добавления, это особенность приложения")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """
        Тест 1: После добавления товара в корзину проверяем, что сообщение об успехе НЕ появилось.
        Ожидаем, что этот тест упадет, так как сообщение появляется сразу.
        """
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message_after_addition()
    
    def test_guest_cant_see_success_message(self, browser):
        """
        Тест 2: При открытии страницы товара проверяем, что сообщение об успехе отсутствует.
        Этот тест должен пройти успешно.
        """
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.xfail(reason="Сообщение об успехе не исчезает после добавления")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        """
        Тест 3: После добавления товара в корзину проверяем, что сообщение об успехе ИСЧЕЗЛО.
        Ожидаем, что этот тест упадет, так как сообщение не исчезает.
        """
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.success_message_should_disappear()