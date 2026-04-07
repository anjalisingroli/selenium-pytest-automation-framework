import pytest
from selenium import webdriver
import os
from config.config import UI_BASE_URL
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(UI_BASE_URL)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs["driver"]
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot("screenshots/failure.png")