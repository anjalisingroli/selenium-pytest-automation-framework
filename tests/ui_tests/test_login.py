# from pages.login_page import LoginPage
#
# def test_valid_login(driver):
#     login = LoginPage(driver)
#     login.enter_username("standard_user")
#     login.enter_password("secret_sauce")
#     login.click_login()
#
#     assert "inventory" in driver.current_url
#
# def test_invalid_login(driver):
#     login = LoginPage(driver)
#     login.enter_username("wrong_user")
#     login.enter_password("wrng_pass")
#     login.click_login()
#
#     assert "inventory" not in driver.current_url

import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", True),
    ("wrong_user", "wrong_pass", False),
])

def test_login(driver, username, password, expected):
    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    if expected:
        assert "inventory" in driver.current_url
    else:
        assert "inventory" not in driver.current_url