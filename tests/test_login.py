import pytest
import allure
from pages.login_page import LoginPage


@allure.feature("Authentication")
@allure.story("Login Logic")
class TestLogin:

    @allure.title("Verify error message for invalid credentials")
    @allure.severity(allure.severity_level.NORMAL)
    def test_failed_login(self, driver):
        login_page = LoginPage(driver)

        with allure.step("Load login page and enter invalid credentials"):
            login_page.load()
            login_page.login("wrong_user", "wrong_pass")

        with allure.step("Verify error message is displayed"):
            error_msg = login_page.find_element(login_page.LOGIN_ERROR).text
            print(f"Captured Error: {error_msg}")
            assert "error" in error_msg.lower() or "not be verified" in error_msg.lower()

    @allure.title("Verify successful login with valid credentials")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)

        with allure.step("Load login page and enter valid credentials"):
            login_page.load()
            # Note: We will move 'john' and 'demo' to a JSON file next!
            login_page.login("john", "demo")

        with allure.step("Verify redirection to Accounts Overview"):
            assert "Accounts Overview" in driver.title
            print("SUCCESS: Logged in as John Demo.")