from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#звпуск драйвера
driver = webdriver.Chrome()

#вариант с исползованием неявного ожидания

#установка
# driver.implicitly_wait(20)
#
# # Переход на сайт
# driver.get("http://uitestingplayground.com/ajax")
#
# # Нажимаем на кнопку
# driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
#
# # Получение текста
# content = driver.find_element(By.CSS_SELECTOR, "#content")
# txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
# print(txt)
#
# # Закрытие браузера
# driver.quit()

# вариант с исползованием явного ожидания

# Переход на сайт
driver.get("http://uitestingplayground.com/ajax")

# Нажимаем на кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Получение текста
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = WebDriverWait(content, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)

print(txt.text)

# Закрытие браузера
driver.quit()