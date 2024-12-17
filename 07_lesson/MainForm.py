from selenium.webdriver.common.by import By

class MainForm:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def __init__(self, driver):
        self.driver = driver

    def webpage(self):
        self.driver.get(self.URL)
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(4)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def send_form(self, first_name, last_name, address, email, phone_number, zip_code, city, country, job_position, company):
        # Заполнение формы
        self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(phone_number)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(company)


    def submit(self):
        # Нажатие на кнопку
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit'").click()

    def get_field_background_color(self, locator):
        element = self.driver.find_element(By.ID, locator)
        return element.value_of_css_property('background-color')

    def close_browser(self):
        self.driver.quit()