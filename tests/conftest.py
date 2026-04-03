from utils.api_client import APIClient
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. Global Variable Initialization
def pytest_configure():
    pytest.shared_account_id = None

# 2. Shared Data Fixture (Session Scope)
@pytest.fixture(scope="session")
def shared_data():
    return {}

# 3. The API Client Fixture (Stand-alone)
@pytest.fixture(scope="session")
def api_client():
    """
    Successfully registered! This is now visible to all tests.
    """
    return APIClient()

# 4. The Browser Driver Fixture
@pytest.fixture(scope="function")
def driver():
    # Setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    yield driver  # The test runs here

    # Teardown
    driver.quit()