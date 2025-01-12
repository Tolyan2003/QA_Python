from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainCalc:
    """
            Этот класс определяет сущность 'Calculator'
            представленный на интернет странице. Клавиши
            нажимаются программно.
    """

    def __init__(self, driver):
        self._driver = driver

    def webpage(self) -> web:
        """
            функция открывает веб-страницу калькулятора на полный экран,
            установлено неявное ожидание и прокрутка всего документа вниз
        """
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.fullscreen_window()
        self._driver.implicitly_wait(4)
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def delay(self) -> int:
        """
            функция находит поле ввода задержки #delay, очищает его
            и в найденное поле вводится число 45
        """
        delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys("45")

    def tap_to_key(self) -> int:
        """
            функция нажимает на клавиатуре калькулятора
            "7", "+", "8", "="
        """
        # Нажатие на кнопки
        self._driver.find_element(By.XPATH, "//span[.='7']").click()
        self._driver.find_element(By.XPATH, "//span[.='+']").click()
        self._driver.find_element(By.XPATH, "//span[.='8']").click()
        self._driver.find_element(By.XPATH, "//span[.='=']").click()

    def itogo(self) -> bool:
        """
            функция через 50 сек определяет результат работы
            калькулятора равный 15
        """
        # Ожидание результата
        result = WebDriverWait(self._driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        return result

    def close_browser(self):
        """
        Функция закрывает открытую веб страницу
        """
        self._driver.quit()
