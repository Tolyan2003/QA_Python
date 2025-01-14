from selenium import webdriver
from MainShop import MainShop
import allure


def test_shop():
    browser = webdriver.Chrome()
    shop = MainShop(browser)

    login = "standard_user"
    password = "secret_sauce"
    first_name = "Иван"
    last_name = "Иванов"
    postcode = "101001"
    expected_total = "Total: $58.29"

    shop.login_to_shop(login, password)
    shop.add_to_cart()
    shop.go_to_cart()
    shop.checkout()
    shop.delivery(first_name, last_name, postcode)
    total = shop.summary_total()

    assert total == expected_total, f"Итоговая сумма не соответствует. Ожидается $58.29, фактически {total}."

    shop.close_browser()
