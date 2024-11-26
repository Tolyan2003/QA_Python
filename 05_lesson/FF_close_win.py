from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Шаг 1: Настройка драйвера Firefox
service = Service(GeckoDriverManager().install())
browser = webdriver.Firefox(service=service)

# Шаг 2: Открытие страницы
url = 'http://the-internet.herokuapp.com/entry_ad'
browser.get(url)

try:
    # Шаг 3: Ожидание появления модального окна
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "modal"))
    )

    # Шаг 4: Ожидаем, пока кнопка станет доступной для взаимодействия
    close_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Close')]"))
    )

    sleep(5)

    # Шаг 5: Нажимаем на кнопку Close
    close_button.click()

except Exception as e:
    print("Ошибка:", str(e))

finally:
    # Задержка перед закрытием браузера
    sleep(5)

    # Закрытие браузера
    browser.quit()