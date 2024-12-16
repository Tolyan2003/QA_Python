
from selenium.webdriver.common.by import By

class AssertForm:
    def __init__(self, driver):
        self._driver = driver

    def fold_color(self):
        # Поля формы после клика
        first_name = self._driver.find_element(By.CSS_SELECTOR, "#first-name")
        last_name = self._driver.find_element(By.CSS_SELECTOR, "#last-name")
        address = self._driver.find_element(By.CSS_SELECTOR, "#address")
        email = self._driver.find_element(By.CSS_SELECTOR, "#e-mail")
        phone_number = self._driver.find_element(By.CSS_SELECTOR, "#phone")
        zip_code = self._driver.find_element(By.CSS_SELECTOR, "#zip-code")
        city = self._driver.find_element(By.CSS_SELECTOR, "#city")
        country = self._driver.find_element(By.CSS_SELECTOR, "#country")
        job_position = self._driver.find_element(By.CSS_SELECTOR, "#job-position")
        company = self._driver.find_element(By.CSS_SELECTOR, "#company")

        # Получение цвета фона полей
        zip_code_color = zip_code.value_of_css_property("background-color")  # Получаем цвет фона для поля ZIP Code
        other_fields_colors = []
        for field in [first_name, last_name, address, email, phone_number, city, country, job_position, company]:
            other_fields_colors.append(field.value_of_css_property("background-color"))

        expected_zip_code_color = "rgba(248, 215, 218, 1)"  # Цвет ошибки (#f8d7da)
        expected_other_fields_color = "rgba(209, 231, 221, 1)"  # Цвет успешного заполнения (#d1e7dd)

        assert zip_code_color == expected_zip_code_color, f"Цвет фона поля ZIP Code неверный. Ожидается {expected_zip_code_color}, получено {zip_code_color}"
        for color in other_fields_colors:
            assert color == expected_other_fields_color, f"Цвет фона одного из полей неверный. Ожидается {expected_other_fields_color}, получено {color}"