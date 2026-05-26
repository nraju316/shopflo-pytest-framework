import pytest

from pages.checkout_page import CheckoutPage
from utils.excel_reader import get_test_data


checkout_test_data = get_test_data(
    "testData/testData.xlsx",
    "checkout"
)


@pytest.mark.parametrize(
    "test_case,"
    "first_name,"
    "last_name,"
    "postal_code,"
    "expected_result",
    checkout_test_data
)
def test_checkout_validation(
        checkout_page_setup,
        test_case,
        first_name,
        last_name,
        postal_code,
        expected_result
):

    if expected_result == "success":

        pytest.skip(
            "Positive checkout handled "
            "in dedicated E2E test"
        )

    checkout_page = CheckoutPage(
        checkout_page_setup
    )

    checkout_page.complete_checkout(
        first_name,
        last_name,
        postal_code
    )

    if expected_result == "first_name_required":

        assert (
            "First Name is required"
            in checkout_page.get_error_message()
        ), (
            "First name validation message mismatch"
        )

    elif expected_result == "last_name_required":

        assert (
            "Last Name is required"
            in checkout_page.get_error_message()
        ), (
            "Last name validation message mismatch"
        )

    elif expected_result == "postal_code_required":

        assert (
            "Postal Code is required"
            in checkout_page.get_error_message()
        ), (
            "Postal code validation message mismatch"
        )