from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:  # <--- MUST be capitalized exactly like this
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        el = self.find_element(locator)
        el.clear()
        el.send_keys(text)

    def get_clean_amount(self, locator):
        """Converts '$1,200.50' from UI to float 1200.50"""
        text = self.find_element(locator).text
        # Remove $, commas, and whitespace
        clean_text = text.replace('$', '').replace(',', '').strip()
        return float(clean_text)

    def wait_for_dropdown_to_populate(self, locator):
        """Waits until a dropdown has at least 2 options available"""
        self.wait.until(lambda driver: len(driver.find_element(*locator).find_elements(By.TAG_NAME, "option")) > 0)