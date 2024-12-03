from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#запуск драйвера
driver = webdriver.Chrome()

#переход на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

#ожидаем загрузку картинок
# wait = driver.find_element(By.CSS_SELECTOR, "#text")
done = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!"))
#берем аттрибуты 4-й картинки
pict_4 = driver.find_element(
    By.CSS_SELECTOR, 'img#landscape').get_dom_attribute("img#landscape")

#вывод атрибутов в консоль
print(pict_4)

# остановка драйвера
driver.quit()