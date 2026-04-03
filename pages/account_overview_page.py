from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class AccountOverviewPage(BasePage):
    # This locator gets the balance of the first account in the table
    FIRST_ACCOUNT_BALANCE = (By.XPATH, "//table[@id='accountTable']//tr[1]/td[2]")
    FIRST_ACCOUNT_LINK = (By.XPATH, "//table[@id='accountTable']//tbody/tr[1]/td[1]/a")
    ACCOUNT_TABLE = (By.ID, "accountTable")

    def wait_for_page_load(self):
        """Wait until the account table is visible on the screen."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ACCOUNT_TABLE)
        )
    def get_first_account_balance(self):
        return self.get_clean_amount(self.FIRST_ACCOUNT_BALANCE)

    def get_first_account_id(self):
        """Extracts the first account number visible in the overview table."""
        element = self.find_element(self.FIRST_ACCOUNT_LINK)
        return element.text.strip()

    def wait_for_balance_to_update(self, expected_value):
        """
        Wait up to 10 seconds for the balance text to match our calculation.
        """
        wait = WebDriverWait(self.driver, 10)

        def check_and_refresh(d):
            # Force a refresh to get the latest data from the server
            d.refresh()
            current = float(self.get_first_account_balance())
            return current == expected_value

        return wait.until(check_and_refresh)

    def is_account_present(self, account_id):
        """Checks if the given ID appears in the Account Overview table"""
        # Dynamic XPath: Searches for the exact text of the ID in any cell
        xpath = (By.XPATH, f"//table[@id='accountTable']//a[text()='{account_id}']")
        try:
            return self.find_element(xpath).is_displayed()
        except:
            return False