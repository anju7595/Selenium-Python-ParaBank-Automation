import pytest
import allure
from utils.api_client import ParaBankAPI


@allure.suite("API Regression Suite")
@allure.feature("Account Services")
class TestAccountAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        """Initialize the API client before each test"""
        self.api = ParaBankAPI()

    @allure.title("Verify New Account Creation via REST API")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_account_successfully(self):
        # 1. Define Test Data
        # Customer 12212 is 'John Doe'. Ensure 13344 is a valid account for him.
        customer_id = "12212"
        from_account_id = "13344"
        account_type = 1  # 1 = Savings

        with allure.step("Send POST request to create account"):
            response = self.api.create_account_api(customer_id, account_type, from_account_id)

        # 2. Assertions
        with allure.step("Validate the API response"):
            # Check status code FIRST to avoid JSON errors
            assert response.status_code == 200, f"API Failed! Status: {response.status_code}, Msg: {response.text}"

            # Now it is safe to parse JSON
            response_data = response.json()

            # Verify ID exists
            assert "id" in response_data, "Response did not contain a new Account ID!"

            # Verify Customer ID ownership
            assert response_data["customerId"] == int(customer_id), \
                f"Expected Customer ID {customer_id}, but got {response_data['customerId']}"

            # Log results
            new_id = response_data["id"]
            allure.attach(f"New Account ID: {new_id}", name="Created ID", attachment_type=allure.attachment_type.TEXT)
            print(f"Successfully created account: {new_id}")