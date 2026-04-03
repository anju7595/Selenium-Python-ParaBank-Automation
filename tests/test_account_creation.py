import allure
import pytest
from config.config import Config # Add this import
from pages.login_page import LoginPage
from pages.open_account_page import OpenAccountPage
from pages.account_overview_page import AccountOverviewPage

@allure.feature("Account Management")
@allure.story("Open New Account")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.order(1)
def test_open_and_verify_new_account(driver):
    # Initialize Pages
    login_page = LoginPage(driver)
    open_page = OpenAccountPage(driver)
    overview_page = AccountOverviewPage(driver)

    with allure.step("Login to ParaBank"):
        login_page.load()
        login_page.login("john", "demo")

    with allure.step("Create New Savings Account"):
        open_page.navigate_to_open_account()
        new_id = open_page.open_savings_account()
        print(f"Created New Account ID: {new_id}")

    with allure.step("Verify Account Presence in Overview"):
        # Use Config here too!
        driver.get(f"{Config.BASE_URL}/overview.htm")
        assert overview_page.is_account_present(new_id), f"Account {new_id} not found!"