from selenium.webdriver.common.by import By

class MainForm:
    def __init__(self, driver):
        self._driver = driver

    def webpage(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.fullscreen_window()
        self._driver.implicitly_wait(4)
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def send_form(self, first_name, last_name, address, email, phone_number, zip_code, city, country, job_position, company):
        # Заполнение формы
        self._driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(address)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(email)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(phone_number)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys(zip_code)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(country)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(job_position)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(company)


    def click(self):
        # Нажатие на кнопку
        self._driver.find_element(By.CSS_SELECTOR, "[type='submit'").click()

    def close_browser(self):
        self._driver.quit()