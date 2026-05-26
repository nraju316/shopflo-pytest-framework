import pytest

from pages.login_page import LoginPage
from utils.excel_reader import get_test_data


test_data = get_test_data(
    "testData/testData.xlsx",
    "all"
)


@pytest.mark.parametrize(
    "test_case,username,password,expected_result",
    test_data
)
def test_login(
        driver,
        test_case,
        username,
        password,
        expected_result
):

    login_page = LoginPage(driver)

    login_page.login(username, password)

    if expected_result == "success":

        assert (
            "inventory" in driver.current_url
        ), "User not navigated to inventory page after successful login"

    elif expected_result == "invalid_credentials":

        assert (
            "do not match any user"
            in login_page.get_error_message()
        ), "Invalid credentials error message mismatch"

    elif expected_result == "locked_out":

        assert (
            "locked out"
            in login_page.get_error_message()
        ), "Locked out user error message mismatch"

    elif expected_result == "username_required":

        assert (
            "Username is required"
            in login_page.get_error_message()
        ), "Username required validation message mismatch"

    elif expected_result == "password_required":

        assert (
            "Password is required"
            in login_page.get_error_message()
        ), "Password required validation message mismatch"