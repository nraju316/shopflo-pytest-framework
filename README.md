# Saucedemo Pytest Automation Framework
![CI](https://github.com/nraju316/shopflo-pytest-framework/actions/workflows/tests.yml/badge.svg)

UI automation framework built using Selenium, Pytest, and the Page Object Model (POM) for automating positive and negative test scenarios on the SauceDemo application.

The framework is designed to be scalable, maintainable, and CI/CD ready with GitHub Actions integration.

## Framework Choice & Why

Tech Stack

- Python 3.12
- Selenium WebDriver
- Pytest
- Pytest HTML Reports
- OpenPyXL
- GitHub Actions

# Why Selenium?

Selenium was chosen because it is one of the most widely used UI automation tools in the industry and provides:

- Cross-browser automation support
- Strong community and ecosystem support
- Easy CI/CD integration
- Flexibility for scalable automation frameworks

Additionally, prior hands-on experience with Selenium helped accelerate framework development and allowed focus on building reusable and maintainable automation components.

It is well suited for real-world web application automation and SDET workflows.

# Why Pytest?

Pytest was chosen because of its:
- Simple and readable syntax
- Powerful fixture support
- Parameterization capabilities
- Scalability for large test suites
- Rich plugin ecosystem

Pytest makes the framework modular, reusable, and easy to maintain.

## Why Page Object Model (POM)?

Page Object Model improves framework maintainability by:
- Separating locators and page actions from test logic
- Reducing code duplication
- Improving readability
- Making tests easier to scale and maintain

Each application page has its own dedicated page class.


## Future Scalability / Extension Plan

The framework is designed to be extensible and can be enhanced further with:

- Parallel execution using pytest-xdist
- Allure reporting integration
- Cross-browser execution
- Docker containerization
- Jenkins pipeline integration
- Retry mechanism for flaky tests
- Database validation support
- Environment-based execution
- Cloud execution using Selenium Grid / BrowserStack

## Automation Coverage

### Login Module
- Valid login
- Invalid credentials
- Locked user validation
- Empty username/password validations

### Inventory Module
- Product visibility validation
- Add/remove cart functionality
- Cart badge validation

### Cart Module
- Product validation inside cart
- Continue shopping flow
- Checkout navigation

### Checkout Module
- Positive checkout flow
- Mandatory field validations
- End-to-end order completion workflow

## Key Highlights

- Selenium + Pytest based automation framework
- Page Object Model (POM) architecture
- Positive and negative test coverage
- Externalized test data management using Excel for scalable data-driven execution
- End-to-End checkout workflow automation
- Screenshot capture on failures
- HTML reporting and logging
- GitHub Actions CI/CD integration
- Headless execution support
- Currently configured for Chrome execution with support for future cross-browser scalability.
- Current automation coverage includes:
  - 18 automated test scenarios
  - Positive, negative, and end-to-end validations

---
## CI/CD Integration

GitHub Actions workflow is configured to automatically execute the test suite on every push and pull request.

Workflow includes:
- Repository checkout
- Python setup
- Dependency installation
- Automated Pytest execution

Headless browser execution is used for CI environments.
## Framework Design Principles

- Reusability
- Scalability
- Maintainability
- Separation of concerns
- CI/CD readiness
- Data-driven execution

---
## Running Tests

Run complete test suite:

```bash
pytest
```

Run specific module:

```bash
pytest tests/test_login.py
```

Generate HTML report:

```bash
pytest --html=reports/report.html
```



# Project Structure

```text
shopflo-pytest-framework/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│           # GitHub Actions workflow for CI execution on push
│
├── pages/
│   ├── base_page.py
│   │   # Base page containing reusable Selenium methods
│   │
│   ├── login_page.py
│   │   # Login page locators and actions
│   │
│   ├── inventory_page.py
│   │   # Inventory/product page actions
│   │
│   ├── cart_page.py
│   │   # Cart page actions and validations
│   │
│   └── checkout_page.py
│       # Checkout flow actions and validations
│
├── tests/
│   ├── test_login.py
│   │   # Positive and negative login test cases
│   │
│   ├── test_inventory.py
│   │   # Inventory module test cases
│   │
│   ├── test_cart.py
│   │   # Cart functionality test cases
│   │
│   ├── test_checkout.py
│   │   # Checkout validation test cases
│   │
│   └── test_e2e_checkout.py
│       # End-to-end checkout workflow validation
│
├── testData/
│   └── testData.xlsx
│       # Externalized Excel test data
│
├── utils/
│   ├── excel_reader.py
│   │   # Reads test data from Excel sheets
│   │
│   ├── logger.py
│   │   # Logging utility configuration
│   │
│   └── screenshot_utils.py
│       # Screenshot capture utility for failed tests
│
├── reports/
│   ├── logs/
│   │   └── test_execution.log
│   │       # Execution logs
│   │
│   └── report.html
│       # Generated Pytest HTML report
│
├── screenshots/
│   # Stores screenshots captured on test failures
│
├── conftest.py
│   # Shared Pytest fixtures, browser setup, hooks, and reusable flows
│
├── config.py
│   # Framework configuration values such as URLs and waits
│
├── pytest.ini
│   # Pytest execution configuration
│
├── requirements.txt
│   # Project dependencies
│
├── .gitignore
│   # Ignored files and folders for Git tracking
│
└── README.md
    # Project documentation
```

Author

Nagaraju K
