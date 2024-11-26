from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


# Шаг 1: Настройка драйвера Firefox
service = Service(GeckoDriverManager().install())
browser = webdriver.Firefox(service=service)

# Шаг 2: Открытие страницы
url = 'http://the-internet.herokuapp.com/login'
browser.get(url)
sleep(2)  # Подождем для загрузки страницы

# Шаг 3: Поиск полей ввода по ID
username_input = browser.find_element(By.ID, 'username')
password_input = browser.find_element(By.ID, 'password')
#         Поиск кнопки по ее типу
login_button = browser.find_element(By.XPATH, "//button[@type='submit']")

# Шаг 4: Ввод значений в поля ввода
username_input.send_keys("tomsmith")
password_input.send_keys("SuperSecretPassword!")
sleep(2)  # Подождем для визуализации

# Шаг 5: Нажать кнопку Login
login_button.click()
sleep(2)  # Подождем для визуализации

# Закрытие браузера
browser.quit()