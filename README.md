# Selenium Pytest Automation Framework

## Overview

This project is a Selenium automation testing framework built using Python and Pytest.
It follows the Page Object Model (POM) design pattern to create maintainable and scalable automated test scripts for web applications.

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)

## Project Structure

```
selenium-pytest-automation-framework
│
├── pages/                  # Page Object classes
│   └── login_page.py       # Login page locators and actions
│
├── tests/                  # Test cases
│   └── test_login.py       # Login test case
│
├── screenshots/            # Failure screenshots
├── reports/                # Test reports
│
├── conftest.py             # Pytest fixtures
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Project dependencies
├── .gitignore              # Ignored files for Git
└── README.md               # Project documentation
```

## Features

* Automated login test cases
* Page Object Model structure
* Pytest test execution
* Automatic screenshot capture on test failure

## How to Run Tests

1. Install dependencies

```
pip install -r requirements.txt
```

2. Run tests

```
pytest
```

## Author

Anjali Singroli
