import allure
import pytest
import json
import os
from config.config import Config
from pages.login_page import LoginPage
from pages.account_overview_page import AccountOverviewPage


# 1. This helper MUST be present to feed data to the decorator
def get_test_data():
    # Adjusted to ensure it finds the file regardless of where you run pytest
    try:
        path = os.path.join(os.getcwd(), "data", "test_data.json")
        with open(path) as f:
            return json.load(f)["test_accounts"]
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return []


@allure.feature("Account Management")
@allure.story("Hybrid API-UI Account Verification")
# 2. This decorator is MANDATORY to define what 'account_data' is
@pytest.mark.parametrize("account_data", get_test_data())
def test_hybrid_account_verification(driver, api_client, account_data):
    login_page = LoginPage(driver)
    overview_page = AccountOverviewPage(driver)

    # STEP 1: Login UI to establish session and find valid data
    with allure.step("UI: Login and find a funding account"):
        login_page.load()
        login_page.login("john", "demo")

        # Grab a real account ID from the table to use as 'fromAccountId'
        funding_id = overview_page.get_first_account_id()

        # Extract Customer ID dynamically from URL or use john's default
        customer_id = 12212

        # STEP 2: Use the dynamic IDs in your API call
    with allure.step(f"API: Create New {account_data['desc']}"):
        response = api_client.create_account(
            customer_id=customer_id,
            account_type=account_data["type"],
            from_account_id=funding_id
        )

        assert response.status_code == 200, f"API Failed! {response.text}"
        new_id = response.json().get("id")
        allure.attach(str(new_id), name="New Account ID")

    # STEP 3: Verify the new account appears in the UI
    with allure.step("UI: Verify Account Presence"):
        driver.get(f"{Config.BASE_URL}/overview.htm")
        overview_page.wait_for_page_load()
        assert overview_page.is_account_present(new_id), f"ID {new_id} not found in UI!"