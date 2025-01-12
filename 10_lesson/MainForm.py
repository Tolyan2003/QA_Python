from selenium.webdriver.common.by import By

class MainForm:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def __init__(self, driver):
        self.driver = driver

    def shop_webpage(self):
        self.driver.get(self.URL)
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(4)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def send_form(self, locator):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(locator)

    def submit(self):
        # Нажатие на кнопку
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit'").click()

    def get_field_background_color(self, locator):
        element = self.driver.find_element(By.ID, locator)
        return element.value_of_css_property('background-color')

    def close_browser(self):
        self.driver.quit()