# Selenium Pytest Automation Framework

## Overview

This project is an automation testing framework built using **Python and Pytest**.
It supports both **UI Automation** and **API Automation** in a single framework.

The framework follows the **Page Object Model (POM)** design pattern for UI testing and uses the **Requests library** for API testing to create maintainable and scalable automated test scripts.

---

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Requests Library
* Page Object Model (POM)
* Git & GitHub

---

## Project Structure

```
selenium-pytest-automation-framework
│
├── pages/                  # Page Object classes for UI
│   └── login_page.py       # Login page locators and actions
│
├── api/                    # API helper functions
│   └── api_helper.py
│
├── tests/
│   ├── ui_tests/           # Selenium UI test cases
│   │   └── test_login.py
│   │
│   └── api_tests/          # API test cases
│       ├── test_get_post.py
│       ├── test_create_post.py
│       ├── test_update_post.py
│       └── test_delete_post.py
│
├── config/
│   └── config.py           # Base URLs and configuration
│
├── screenshots/            # Failure screenshots
├── reports/                # HTML test reports
│
├── conftest.py             # Pytest fixtures
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Project dependencies
├── .gitignore              # Ignored files for Git
└── README.md               # Project documentation
```

---

## Features

* UI automation using Selenium WebDriver
* API automation using Requests library
* Page Object Model (POM) structure
* Pytest test execution
* Parametrized test cases
* HTML test reports
* Automatic screenshot capture on test failure
* Organized UI and API test structure

---

## Automation Workflow

### UI Automation Workflow

```
Test Case (Pytest)
        │
        ▼
Page Object Model (pages folder)
        │
        ▼
Selenium WebDriver
        │
        ▼
Web Application
        │
        ▼
Test Result
        │
        ▼
Reports & Screenshots
```

---

### API Automation Workflow

```
Test Case (Pytest)
        │
        ▼
API Helper Functions
        │
        ▼
Requests Library
        │
        ▼
API Endpoint
        │
        ▼
Response Validation
        │
        ▼
Test Result
```

---

## Installation

### 1 Clone the repository

```
git clone https://github.com/anjalisingroli/selenium-pytest-automation-framework.git
```

### 2 Navigate to the project folder

```
cd selenium-pytest-automation-framework
```

### 3 Install required dependencies

```
pip install -r requirements.txt
```

---

## How to Run Tests

Run all tests:

```
pytest
```

Run only API tests:

```
pytest -m api
```

Run only UI tests:

```
pytest -m ui
```

---

## Reports

After test execution, HTML reports will be generated inside the **reports** folder.

Example location:

```
reports/report.html
```

---

## Screenshots

If any UI test fails, screenshots are automatically captured and stored inside the **screenshots** folder.

---

## Author

Anjali Singroli
