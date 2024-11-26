from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


# Шаг 1: Настройка драйвера Firefox
service = Service(GeckoDriverManager().install())
browser = webdriver.Firefox(service=service)

# Шаг 2: Открытие страницы
url = 'http://the-internet.herokuapp.com/inputs'
browser.get(url)
sleep(2)  # Подождем для загрузки страницы

# Шаг 3: Поиск поля ввода
input_field = browser.find_element(By.CSS_SELECTOR, 'input')

# Шаг 4: Ввод текста "1000" в поле
input_field.send_keys("1000")
sleep(2)  # Подождем для визуализации

# Шаг 5: Очистка поля (методом clear)
input_field.clear()
sleep(2)  # Подождем для визуализации

# Шаг 6: Ввод текста "999" в очищенное поле
input_field.send_keys("999")
sleep(2)  # Подождем для визуализации

# Закрытие браузера
browser.quit()