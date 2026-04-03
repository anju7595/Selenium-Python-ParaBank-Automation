# Selenium Python ParaBank Automation

An automated testing framework designed for the ParaBank application using **Python**, **Selenium**, and **Pytest**. This project demonstrates a scalable **Page Object Model (POM)** architecture tailored for financial/banking application workflows.

## 🚀 Features
* **Design Pattern:** Page Object Model (POM) for enhanced maintainability.
* **Testing Tool:** Selenium WebDriver with Python.
* **Test Runner:** Pytest for execution and assertions.
* **Reporting:** Integrated with Allure Reports (optional) for detailed test insights.
* **Dynamic Locators:** Efficient use of XPATH and ID strategies for stable element interaction.

## 📁 Project Structure
- `pages/`: Contains page classes with locators and page-specific methods (e.g., `account_overview_page.py`).
- `tests/`: Contains the test scripts (e.g., `test_hybrid_account.py`).
- `test_data.json`: Centralized location for managing test input values.
- `conftest.py`: Manages fixture setup/teardown and WebDriver initialization.

## 🛠️ Prerequisites
* Python 3.14+
* Chrome/Edge/Firefox browser installed
* Appropriate WebDriver (managed automatically via `webdriver-manager` recommended)

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/Selenium-Python-ParaBank-Automation.git](https://github.com/your-username/Selenium-Python-ParaBank-Automation.git)
   
2. Navigate to the project directory:
cd Selenium-Python-ParaBank-Automation
3. Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
4. Install dependencies:
pip install -r requirements.txt


🏃 Running Tests
To run all tests in the project: pytest
To run a specific test file: pytest tests/test_hybrid_account.py

📊 Key Workflows Covered
Account Overview: Validating balances and account links.

Account Creation: Automating the opening of new checking/savings accounts.

Fund Transfers: Verifying transaction logic between accounts.