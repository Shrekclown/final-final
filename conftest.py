import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    """Фикстура для запуска браузера"""
    print("\n🚀 Запуск браузера для теста...")
    options = Options()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\n🔚 Закрытие браузера...")
    browser.quit()