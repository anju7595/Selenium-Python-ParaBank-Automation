from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class OpenAccountPage(BasePage):
    # Locators
    OPEN_ACCOUNT_LINK = (By.LINK_TEXT, "Open New Account")
    ACCOUNT_TYPE_DROPDOWN = (By.ID, "type")
    EXISTING_ACCOUNT_DROPDOWN = (By.ID, "fromAccountId")
    OPEN_BUTTON = (By.XPATH, "//input[@value='Open New Account']")
    NEW_ACCOUNT_ID = (By.ID, "newAccountId")

    def navigate_to_open_account(self):
        self.click_element(self.OPEN_ACCOUNT_LINK)

    def open_savings_account(self):
        # Select 'SAVINGS' (Index 1)
        select_type = Select(self.find_element(self.ACCOUNT_TYPE_DROPDOWN))
        select_type.select_by_index(1)

        # Wait for the account list to load before clicking
        self.wait_for_dropdown_to_populate(self.EXISTING_ACCOUNT_DROPDOWN)

        self.click_element(self.OPEN_BUTTON)

        # Return the new ID so the test can verify it later
        return self.find_element(self.NEW_ACCOUNT_ID).text