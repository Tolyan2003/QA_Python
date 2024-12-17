from selenium import webdriver
from MainForm import MainForm
# from AssertForm import AssertForm

def test_form():
    driver = webdriver.Chrome()
    main_form = MainForm(driver)

    first_name = "Иван"
    last_name = "Петров"
    address = "Ленина, 55-3"
    email = "test@skypro.com"
    phone_number = "+7985899998787"
    zip_code = ""
    city = "Москва"
    country = "Россия"
    job_position = "QA"
    company = "SkyPro"

    main_form.webpage()
    main_form.send_form(first_name, last_name, address, email, phone_number, zip_code, city, country, job_position, company)
    main_form.submit()

    # Получение цветов полей
    first_name = "first-name"
    last_name = "last-name"
    address = "address"
    email = "e-mail"
    phone_number = "phone"
    zip_code = "zip-code"
    city = "city"
    country = "country"
    job_position = "job-position"
    company = "company"

    zip_code_color = main_form.get_field_background_color(zip_code)  # Получаем цвет фона для поля ZIP Code
    other_fields_colors = [
        main_form.get_field_background_color(element)
        for element in [first_name, last_name, address, email, phone_number, city, country, job_position, company]
    ]
    # Проверка цветов полей
    expected_zip_code_color = "rgba(248, 215, 218, 1)"  # Цвет ошибки (#f8d7da)
    expected_other_fields_color = "rgba(209, 231, 221, 1)"  # Цвет успешного заполнения (#d1e7dd)

    assert zip_code_color == expected_zip_code_color, f"Цвет фона поля ZIP Code неверный. Ожидается {expected_zip_code_color}, получено {zip_code_color}"
    for color in other_fields_colors:
        assert color == expected_other_fields_color, f"Цвет фона одного из полей неверный. Ожидается {expected_other_fields_color}, получено {color}"

    main_form.close_browser()







