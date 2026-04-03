from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage

class TransferPage(BasePage):
    TRANSFER_LINK = (By.LINK_TEXT, "Transfer Funds")
    AMOUNT_INPUT = (By.ID, "amount")
    FROM_ACCOUNT_SELECT = (By.ID, "fromAccountId")
    TO_ACCOUNT_SELECT = (By.ID, "toAccountId")
    TRANSFER_BUTTON = (By.XPATH, "//input[@value='Transfer']")

    def navigate_to_transfer(self):
        self.click_element(self.TRANSFER_LINK)
        # Ensure accounts are loaded
        self.wait_for_dropdown_to_populate(self.FROM_ACCOUNT_SELECT)

    def select_different_accounts(self):
        """Selects two different accounts to ensure the balance actually moves"""
        from_dropdown = Select(self.find_element(self.FROM_ACCOUNT_SELECT))
        to_dropdown = Select(self.find_element(self.TO_ACCOUNT_SELECT))

        # Select the 1st option for 'From'
        from_dropdown.select_by_index(0)
        from_account_id = from_dropdown.first_selected_option.text

        # Select the 2nd option for 'To' (if available)
        if len(to_dropdown.options) > 1:
            to_dropdown.select_by_index(1)

        to_account_id = to_dropdown.first_selected_option.text
        print(f"Transferring FROM: {from_account_id} TO: {to_account_id}")

        return from_account_id == to_account_id  # Returns True if they are the same (oops!)

    def perform_transfer(self, amount):
        self.type_text(self.AMOUNT_INPUT, str(amount))
        self.click_element(self.TRANSFER_BUTTON)