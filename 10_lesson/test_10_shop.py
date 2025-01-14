from selenium import webdriver
from MainShop import MainShop
import allure

@allure.id("QA_Shop")
@allure.story("Покупка в интернет-магазине")
@allure.title("Тестирование процесса покупки")
@allure.feature("Develop")
@allure.description(""" Тестирует весь процесс покупки в интернет-магазине: вход, добавление товаров в корзину, оформление заказа и проверка итоговой суммы. """)
def test_shop():
    with allure.step("Запуск браузера"):
        browser = webdriver.Chrome()

    with allure.step("Создание объекта интернет-магазина"):
        shop = MainShop(browser)

    with allure.step("Данные для входа"):
        login = "standard_user"
        password = "secret_sauce"
        first_name = "Иван"
        last_name = "Иванов"
        postcode = "101001"
        expected_total = "Total: $58.29"

    with allure.step("Авторизация в магазине"):
        shop.login_to_shop(login, password)

    with allure.step("Добавление товаров в корзину"):
        shop.add_to_cart()

    with allure.step("Переход в корзину"):
        shop.go_to_cart()

    with allure.step("Начать оформление заказа"):
        shop.checkout()

    with allure.step("Оформление доставки"):
        shop.delivery(first_name, last_name, postcode)

    with allure.step("Получение итоговой суммы"):
        total = shop.summary_total()

    with allure.step("Проверка итоговой суммы"):
        assert total == expected_total, f"Итоговая сумма не соответствует. Ожидается $58.29, фактически {total}."

    with allure.step("Закрытие браузера"):
        shop.close_browser()
