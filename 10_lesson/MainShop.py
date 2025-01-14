from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path
import allure

@allure.epic("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://www.saucedemo.com/", name="Интернет магазин")
class MainShop:
    """ Класс описывает функциональность интернет-магазина для тестирования покупок: авторизация при входе, добавление товара в корзину, оформление доставки и проверка суммы покупки. """

    def __init__(self, driver):
        """ Инициализация драйвера Selenium и открытие главной страницы магазина. :param driver: экземпляр WebDriver """
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    @allure.step("Авторизация в магазине")
    def login_to_shop(self, username: str, password: str):
        """ Авторизация пользователя в интернет-магазине. :param username: имя пользователя :param password: пароль """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name"))
        ).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self):
        """ Добавляет товары в корзину. """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))
        ).click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """ Переходит в корзину. """
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    @allure.step("Начало оформления заказа")
    def checkout(self):
        """ Начинает процесс оформления заказа. """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
        ).click()

    @allure.step("Оформление доставки")
    def delivery(self, first_name: str, last_name: str, postal_code: str):
        """ Оформляет доставку. :param first_name: имя :param last_name: фамилия :param postal_code: почтовый индекс """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получение итоговой суммы")
    def summary_total(self) -> str:
        """ Считывает итоговую сумму покупки. :return: Итоговая сумма """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        total_price = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_price.text

    @allure.step("Закрытие браузера")
    def close_browser(self):
        """ Закрывает браузер. """
        self.driver.quit()