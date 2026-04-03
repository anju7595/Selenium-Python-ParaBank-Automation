
from selenium.webdriver.common.by import By

from config.config import Config
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators (Stored as Tuples)
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")
    LOGIN_ERROR = (By.CLASS_NAME, "error")

    def __init__(self, driver):
        super().__init__(driver)
        # Use the config variable instead of a hardcoded string
        self.url = f"{Config.BASE_URL}/index.htm"

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.type_text(self.USERNAME_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)