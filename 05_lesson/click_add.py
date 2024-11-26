from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Шаг 1: Открываем страницу
url = 'http://the-internet.herokuapp.com/add_remove_elements/'
browser = webdriver.Chrome()
browser.get(url)
sleep(2)  # Подождем пару секунд для загрузки страницы

# Шаг 2: Пять раз кликаем на кнопку Add Element
add_button = browser.find_element(By.XPATH, '//button[contains(text(),"Add Element")]')
for _ in range(5):
    add_button.click()
    sleep(1)  # Небольшая пауза между кликами

# Шаг 3: Собираем список кнопок Delete
delete_buttons = browser.find_elements(By.XPATH, '//button[contains(text(),"Delete")]')

# Шаг 4: Выводим на экран размер списка
print(f'Количество кнопок Delete: {len(delete_buttons)}')

# Закрытие браузера
browser.quit()