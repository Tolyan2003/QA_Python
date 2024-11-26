from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Шаг 1: Открываем страницу
url = 'http://uitestingplayground.com/dynamicid'
browser = webdriver.Chrome()
browser.get(url)
sleep(2)  # Подождем пару секунд для загрузки страницы


# Шаг 2: Найти и кликнуть на синюю кнопку
blue_button = browser.find_element(By.XPATH, '//button[contains(text(),"Button with Dynamic ID")]').click()

# Ждем немного перед закрытием браузера
sleep(5)

# Закрытие браузера
browser.quit()
