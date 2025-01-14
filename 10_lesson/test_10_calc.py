from selenium import webdriver
from MainCalc import MainCalc
import allure

@allure.id("QA_Calc")
@allure.story("Проведение вычислений")
@allure.feature("Calc")
@allure.title("Программный калькулятор")
@allure.description(""" Вычисление результата при вводе значений в калькулятор программно с учетом времени ожидания """)
def test_calc():
    with allure.step("Запускаем Chrome"):
        browser = webdriver.Chrome()

    with allure.step("Инициализируем объект калькулятора"):
        calc = MainCalc(browser)

    with allure.step("Открываем веб-страницу калькулятора"):
        calc.open_calculator_page()

    with allure.step("Устанавливаем задержку 10 секунд"):
        calc.set_delay()

    with allure.step("Последовательность нажатий клавиш"):
        calc.press_buttons(["7", "+", "8", "="])

    with allure.step("Ожидаем результат"):
        result = calc.get_result(20)

    with allure.step("Проверяем полученный результат"):
        assert result, "Результат не отображается!"

    with allure.step("Закрываем браузер"):
        calc.close_browser()