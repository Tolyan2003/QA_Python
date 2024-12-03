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
pict_3 = driver.find_element(
    By.CSS_SELECTOR, 'img#award')

#вывод атрибутов в консоль
print(pict_3.get_dom_attribute("src"))

# остановка драйвера
driver.quit()