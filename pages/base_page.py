from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

class BasePage:
    """Базовый класс для всех Page Objects"""
    
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    def open(self):
        """Открывает страницу"""
        self.browser.get(self.url)
    
    def is_element_present(self, how, what):
        """Проверяет наличие элемента на странице (мгновенно)"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def is_not_element_present(self, how, what, timeout=4):
        """
        Проверяет, что элемент НЕ появляется на странице в течение timeout секунд.
        
        Использование: когда элемент потенциально может появиться, но не должен.
        
        Args:
            how: стратегия поиска (By.ID, By.CSS_SELECTOR и т.д.)
            what: селектор элемента
            timeout: время ожидания в секундах
            
        Returns:
            True если элемент НЕ появился за отведённое время
            False если элемент появился
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            # Элемент не появился - это хорошо для отрицательной проверки
            return True
        
        # Элемент появился - тест должен упасть
        return False
    
    def is_disappeared(self, how, what, timeout=4):
        """
        Проверяет, что элемент ИСЧЕЗАЕТ со страницы в течение timeout секунд.
        
        Использование: когда элемент был на странице и должен исчезнуть.
        
        Args:
            how: стратегия поиска
            what: селектор элемента
            timeout: время ожидания в секундах
            
        Returns:
            True если элемент исчез за отведённое время
            False если элемент всё ещё присутствует
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            # Элемент не исчез - тест должен упасть
            return False
        
        # Элемент исчез - успех
        return True
    
    def solve_quiz_and_get_code(self):
        """Решает математическое выражение в алерте и возвращает код"""
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