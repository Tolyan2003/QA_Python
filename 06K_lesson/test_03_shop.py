import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

# test
def test_03_shop(driver):
    driver.get("https://www.saucedemo.com/")
    driver.fullscreen_window()

    # Авторизация
    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name"))).send_keys("standard_user")
    password_field = driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    # username_field.send_keys("standard_user")
    # password_field.send_keys("secret_sauce")
    # login_button.click()

    # Добавление товаров в корзину
    add_backpack_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))).click()
    add_tshirt_button = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    add_onesie_button = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    # add_backpack_button.click()
    # add_tshirt_button.click()
    # add_onesie_button.click()

    # Переход в корзину
    cart_icon = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    # cart_icon.click()

    # Перейти к оформлению заказа
    checkout_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout"))).click()
    # checkout_button.click()

    # Заполнить информацию о доставке
    first_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Иван")
    last_name_field = driver.find_element(By.ID, "last-name").send_keys("Иванов")
    postal_code_field = driver.find_element(By.ID, "postal-code").send_keys("101001")
    continue_button = driver.find_element(By.ID, "continue").click()

    # first_name_field.send_keys("Иван")
    # last_name_field.send_keys("Иванов")
    # postal_code_field.send_keys("101001")
    # continue_button.click()

    # Прочитать итоговую сумму
    total_price = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))).text

    # Проверка итоговой суммы
    assert total_price == "Total: $58.29", f"Итоговая сумма не соответствует. Ожидается $58.29, фактически {total_price}."