#the test cases
import pytest
from pages.login_page import LoginPage

#positive test case
def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url          # landed on products page
#negative test case
def test_invalid_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "wrong_pass")
    assert "do not match" in page.get_error()

@pytest.mark.parametrize("user, pwd, expected", [
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("locked_out_user", "secret_sauce", "locked out"),
])
def test_login_negative(driver, user, pwd, expected):
    page = LoginPage(driver)
    page.open()
    page.login(user, pwd)
    assert expected in page.get_error()