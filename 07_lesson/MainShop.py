from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainShop:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    def login_to_shop(self, login, password):
        # Авторизация
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name"))).send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def add_to_cart(self):
        # Добавление товаров в корзину
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))
        ).click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        # Переход в корзину
        self._driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    def checkout(self):
        # Перейти к оформлению заказа
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
        ).click()

    def delivery(self, first_name, last_name, postcode):
        # Заполнение информации о доставке
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(postcode)
        self._driver.find_element(By.ID, "continue").click()

    def summary_total(self):
        # Прочитать итоговую сумму
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        total_price = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_price.text

    def close_browser(self):
        self._driver.quit()