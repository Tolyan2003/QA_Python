from selenium.webdriver.common.by import By
import  allure


@allure.epic("форма заполнения")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://bonigarcia.dev/selenium-webdriver-java/data-types.html", name="Веб-форма")
class MainForm:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    """
            Этот класс определяет сущность 'MainForm', web-формы
            представленной на интернет странице "Hands-On Selenium WebDriver". Формы заполняются из 
            словаря, где ключи это локаторы, а значения – данные для ввода
    """
    def __init__(self, driver):
        """
        метод активации selenium
        """
        self.driver = driver

    def shop_webpage(self):
        """
        метод открытия веб-страницы с формами
        """
        self.driver.get(self.URL)
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(4)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def send_form(self, locator: str, value: str):
        """
        метод заполнения форм из словаря
        ключ - локатор;
        значение - данные для ввода
        """
        self.driver.find_element(By.CSS_SELECTOR, locator).send_keys(value)

    def submit(self):
        """
        метод нажатия на кнопку 'submit'
        """
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    def get_field_background_color(self, locator: str) -> int:
        """
        метод определения цвета полей формы
        """
        element = self.driver.find_element(By.ID, locator)
        return element.value_of_css_property('background-color')

    def close_browser(self):
        """
        метод закрытия браузера
        """
        self.driver.quit()