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
def test_02_calc(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.fullscreen_window()

    # Ввод значения задержки
    delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay.clear()
    delay.send_keys("45")

    # Нажатие на кнопки
    seven_button = driver.find_element(By.XPATH, "//span[.='7']").click()
    plus_button = driver.find_element(By.XPATH, "//span[.='+']").click()
    eight_button = driver.find_element(By.XPATH, "//span[.='8']").click()
    equals_button = driver.find_element(By.XPATH, "//span[.='=']").click()

    # seven_button.click()
    # plus_button.click()
    # eight_button.click()
    # equals_button.click()

    # Ожидание результата

    result = WebDriverWait(driver, 50).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    # Проверка результата
    assert result, "Результат не отображается!"