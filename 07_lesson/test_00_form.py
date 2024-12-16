from selenium import webdriver
from MainForm import MainForm
from AssertForm import AssertForm

def test_form():
    browser = webdriver.Chrome()
    main_form = MainForm(browser)
    assert_form = AssertForm(browser)

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
    main_form.click()
    assert_form.fold_color()

    main_form.close_browser()







