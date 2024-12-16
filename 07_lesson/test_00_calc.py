from selenium import webdriver
from MaimCalc import MainCalc


# test
def test_calc():
    browser = webdriver.Chrome()
    calc = MainCalc(browser)

    calc.webpage()
    calc.delay()
    calc.tap_to_key()
    result = calc.itogo()

    # Проверка результата
    assert result, "Результат не отображается!"

    calc.close_browser()