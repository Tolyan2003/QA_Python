from selenium import webdriver
from selenium.webdriver.common.by import By

#звпуск драйвера
driver = webdriver.Chrome()

#переход на сайт
driver.get("http://uitestingplayground.com/textinput")

#поиск строки
new_buttonname = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

# ввод текста SkyPro
new_buttonname.send_keys("SkyPro")

# поиск кнопки
new_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")

# нажать на кнопку
new_button.click()
print(new_button.text)

# остановить драйвер
driver.quit()