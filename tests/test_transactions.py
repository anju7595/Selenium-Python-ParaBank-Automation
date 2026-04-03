import pytest
import allure
from config.config import Config
from pages.login_page import LoginPage
from pages.account_overview_page import AccountOverviewPage
from pages.transfer_page import TransferPage


@allure.feature("Payments")
@allure.story("Fund Transfer Consistency")
@pytest.mark.order(2)
def test_transfer_balance_consistency(driver):
    login_page = LoginPage(driver)
    overview_page = AccountOverviewPage(driver)
    transfer_page = TransferPage(driver)

    with allure.step("Login and capture initial balance"):
        login_page.load()
        login_page.login("john", "demo")
        initial_balance = overview_page.get_first_account_balance()
        allure.attach(f"Initial Balance: {initial_balance}", name="Balance Info",
                      attachment_type=allure.attachment_type.TEXT)

    with allure.step("Navigate to Transfer and select distinct accounts"):
        transfer_page.navigate_to_transfer()
        is_same = transfer_page.select_different_accounts()
        if is_same:
            pytest.skip("Only one account found; skipping cross-account transfer test.")

    with allure.step("Perform transfer of $100.00"):
        transfer_amount = 100.00
        transfer_page.perform_transfer(transfer_amount)

    with allure.step("Verify balance deduction in Overview"):
        # Professional move: Use the Config URL
        driver.get(f"{Config.BASE_URL}/overview.htm")
        new_balance = overview_page.get_first_account_balance()

        expected_balance = initial_balance - transfer_amount

        # Adding context to the assertion for easier debugging
        assert new_balance == expected_balance, \
            f"Balance Mismatch! Initial: {initial_balance}, Transferred: {transfer_amount}, Expected: {expected_balance}, Actual: {new_balance}"