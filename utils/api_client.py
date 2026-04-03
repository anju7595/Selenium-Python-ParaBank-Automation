import requests
from config.config import Config


class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {"Accept": "application/json"}

    # Add this method to fix the AttributeError
    def post(self, url, params=None, json=None):
        return self.session.post(url, params=params, json=json, headers=self.headers)

    def create_account(self, customer_id, account_type=1, from_account_id="13344"):
        # Ensure URL is correct - ParaBank usually uses /services_proxy/ or /services/bank/
        url = f"{Config.BASE_URL}/services/bank/createAccount"

        params = {
            "customerId": customer_id,
            "newAccountType": account_type,
            "fromAccountId": from_account_id
        }

        # Explicitly passing params to requests.post sends them as a query string:
        # URL?customerId=...&newAccountType=...
        response = self.session.post(url, params=params, headers=self.headers)

        # Debugging: If it still fails, let's see why
        if response.status_code != 200:
            print(f"DEBUG: API Error Response: {response.text}")

        return response