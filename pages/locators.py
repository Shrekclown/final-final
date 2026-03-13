from selenium.webdriver.common.by import By

class BasePageLocators:
    """Базовые локаторы для всех страниц"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class ProductPageLocators:
    """Локаторы для страницы товара"""
    
    # Кнопка добавления в корзину
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    
    # Название товара (в карточке товара)
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    
    # Цена товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    
    # Сообщение о добавлении в корзину (название товара)
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    
    # Сообщение со стоимостью корзины
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    
    # Сообщение об успехе (сам элемент сообщения)
    SUCCESS_MESSAGE_ELEMENT = (By.CSS_SELECTOR, ".alert-success")