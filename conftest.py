import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """Добавляет параметр командной строки --language"""
    parser.addoption(
        '--language',
        action='store',
        default='en',  # язык по умолчанию
        help="Choose language: es, fr, ru, etc."
    )

@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для запуска браузера с указанным языком"""
    # Получаем параметр language из командной строки
    user_language = request.config.getoption("language")
    print(f"\n🌐 Запуск браузера с языком: {user_language}")
    
    # Настраиваем опции Chrome для нужного языка
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )
    
    # Создаем экземпляр браузера
    browser = webdriver.Chrome(options=options)
    
    # Возвращаем браузер для использования в тестах
    yield browser
    
    # Закрываем браузер после теста
    print("\n🔚 Закрытие браузера...")
    browser.quit()