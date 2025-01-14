from selenium import webdriver
from MainForm import MainForm
import allure


@allure.id("QA_Form")
@allure.story("Формы для заполнения")
@allure.feature("Form")
@allure.title("Форма с полями")
@allure.description("Форма с полями для внесения данных. В случае не внесения данных в ячейку после нажатия кнопки "
                    "'submit' она подсвечивается красным оттенком]")
def test_form():
    with allure.step("открытие веб-формы для внесения данных"):
        driver = webdriver.Chrome()
        main_form = MainForm(driver)
        main_form.shop_webpage()

    with allure.step("словарь - поля и данные для внесения"):
        fields_data = {
            "input[name='first-name']": "Иван",
            "input[name='last-name']": "Петров",
            "input[name='address']": "Ленина, 55-3",
            "input[name='e-mail']": "test@skypro.com",
            "input[name='phone']": "+7985899998787",
            "input[name='zip-code']": "",
            "input[name='city']": "Москва",
            "input[name='country']": "Россия",
            "input[name='job-position']": "QA",
            "input[name='company']": "SkyPro"
        }

    with allure.step("Внесение данных из словаря"):
        for locator, value in fields_data.items():
            with allure.step(f"Внести данные в поле '{locator}' со значением '{value}'"):
                main_form.send_form(locator, value)

    main_form.submit()

    with allure.step("Названия полей после нажатия кнопки 'submit'"):
        field_names = ["first-name", "last-name", "address",
                       "e-mail", "phone", "zip-code", "city",
                       "country", "job-position", "company"]

    with allure.step("Определение цвета ячеек"):
        colors = {}
        for name in field_names:
            with allure.step(f"Получить цвет фона для поля '{name}'"):
                colors[name] = main_form.get_field_background_color(name)

    with allure.step("Установка ожидаемых цветов 'успех' и 'ошибка'"):
        expected_error_color = "rgba(248, 215, 218, 1)"  # Цвет ошибки (#f8d7da)
        expected_success_color = "rgba(209, 231, 221, 1)"  # Цвет успешного заполнения (#d1e7dd)

    with allure.step("Проверка цветов полей"):
        for name, color in colors.items():
            if name == "zip-code":
                with allure.step(f"Проверить цвет поля '{name}'. Ожидаемый цвет ошибки: {expected_error_color}"):
                    assert color == expected_error_color, f"Цвет фона поля '{name}' неверный. Ожидается {expected_error_color}, получено {color}"
            else:
                with allure.step(f"Проверить цвет поля '{name}'. Ожидаемый цвет успеха: {expected_success_color}"):
                    assert color == expected_success_color, f"Цвет фона поля '{name}' неверный. Ожидается {expected_success_color}, получено {color}"

    with allure.step("Закрыть браузер"):
        main_form.close_browser()