class BasePage():
    """Базовый класс для всех Page Objects"""
    
    def __init__(self, browser, url):
        """
        Конструктор класса BasePage
        
        Args:
            browser: экземпляр драйвера браузера
            url: адрес страницы
        """
        self.browser = browser
        self.url = url
    
    def open(self):
        """Открывает страницу в браузере"""
        self.browser.get(self.url)