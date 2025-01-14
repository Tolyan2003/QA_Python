from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

@allure.epic("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html", name="Калькулятор")
class MainCalc:
    """ Класс описывает функциональность калькулятора на веб-странице.
        Кнопки калькулятора нажимаются программно.
        Учитывается время ожидания до получения результата.
    """

    def __init__(self, driver):
        """ Инициализация драйвера Selenium. :param driver: экземпляр WebDriver """
        self.driver = driver

    @allure.step("Открытие страницы калькулятора")
    def open_calculator_page(self):
        """ Открывает страницу калькулятора на полный экран, устанавливает неявное ожидание и прокручивает документ вниз. """
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(14)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step("Установка значения задержки")
    def set_delay(self, delay_value=10):
        """ Устанавливает значение задержки в поле ввода.
            :param delay_value: значение задержки (по умолчанию 10 секунд)
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay_value)

    @allure.step("Нажатие последовательности кнопок {sequence}")
    def press_buttons(self, sequence):
        """ Последовательно нажимает указанные кнопки на калькуляторе. :param sequence: список кнопок для нажатия """
        for button in sequence:
            with allure.step(f"Нажатие кнопки '{button}'"):
                self.driver.find_element(By.XPATH, f"//span[.='{button}']").click()

    @allure.step("Получение результата")
    def get_result(self, timeout=15) -> bool:

        result = WebDriverWait(self.driver, timeout).until(
                 EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        return result

    @allure.step("Закрытие браузера")
    def close_browser(self):
        """ Закрывает браузер. """
        self.driver.quit()