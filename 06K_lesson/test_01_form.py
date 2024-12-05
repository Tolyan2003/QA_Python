import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


# Тест
def test_01_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.fullscreen_window()

    # Заполнение формы
    first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
    first_name.clear()
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
    last_name.clear()
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
    address.clear()
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
    email.clear()
    email.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
    phone_number.clear()
    phone_number.send_keys("+7985899998787")

    zip_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
    zip_code.clear()
    zip_code.send_keys("")

    city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
    city.clear()
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
    country.clear()
    country.send_keys("Россия")

    job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
    job_position.clear()
    job_position.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
    company.clear()
    company.send_keys("SkyPro")

    # Нажатие на кнопку
    driver.find_element(By.CSS_SELECTOR, "[type='submit'").click()

    # Поля формы после клика
    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    address = driver.find_element(By.CSS_SELECTOR, "#address")
    email = driver.find_element(By.CSS_SELECTOR, "#e-mail")
    phone_number = driver.find_element(By.CSS_SELECTOR, "#phone")
    zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    city = driver.find_element(By.CSS_SELECTOR, "#city")
    country = driver.find_element(By.CSS_SELECTOR, "#country")
    job_position = driver.find_element(By.CSS_SELECTOR, "#job-position")
    company = driver.find_element(By.CSS_SELECTOR, "#company")

    # Получение цвета фона полей
    zip_code_color = zip_code.value_of_css_property("background-color")  # Получаем цвет фона для поля ZIP Code
    other_fields_colors = []
    for field in [first_name, last_name, address, email, phone_number, city, country, job_position, company]:
        other_fields_colors.append(field.value_of_css_property("background-color"))

    # Проверка цветов полей
    expected_zip_code_color = "rgba(248, 215, 218, 1)"  # Цвет ошибки (#f8d7da)
    expected_other_fields_color = "rgba(209, 231, 221, 1)"  # Цвет успешного заполнения (#d1e7dd)

    assert zip_code_color == expected_zip_code_color, f"Цвет фона поля ZIP Code неверный. Ожидается {expected_zip_code_color}, получено {zip_code_color}"
    for color in other_fields_colors:
        assert color == expected_other_fields_color, f"Цвет фона одного из полей неверный. Ожидается {expected_other_fields_color}, получено {color}"
