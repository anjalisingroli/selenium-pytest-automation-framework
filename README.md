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

## Installation

1. Clone the repository

```
git clone https://github.com/anjalisingroli/selenium-pytest-automation-framework.git
```

2. Navigate to the project folder

```
cd selenium-pytest-automation-framework
```

3. Install required dependencies

```
pip install -r requirements.txt
```

## How to Run Tests

Run all test cases using:

```
pytest
```

## Reports

After test execution, HTML reports will be generated inside the **reports** folder.

## Screenshots

If any test fails, screenshots are automatically captured and stored inside the **screenshots** folder.

## Author

Anjali Singroli
