import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.excel_reader import get_test_data


e2e_test_data = get_test_data(
    "testData/testData.xlsx",
    "e2e_checkout"
)


@pytest.mark.parametrize(
    "test_case,"
    "first_name,"
    "last_name,"
    "postal_code",
    e2e_test_data
)
def test_complete_checkout_flow(
        cart_with_product,
        test_case,
        first_name,
        last_name,
        postal_code
):

    inventory_page = InventoryPage(
        cart_with_product
    )

    # Step 1:
    # Open cart page

    inventory_page.open_cart()

    cart_page = CartPage(
        cart_with_product
    )

    # Step 2:
    # Validate cart item exists

    assert (
        len(cart_page.get_cart_items()) == 1
    ), "Cart item count mismatch"

    # Step 3:
    # Navigate to checkout

    cart_page.click_checkout()

    checkout_page = CheckoutPage(
        cart_with_product
    )

    # Step 4:
    # Enter checkout information

    checkout_page.complete_checkout(
        first_name,
        last_name,
        postal_code
    )

    # Step 5:
    # Validate overview page

    assert (
        "checkout-step-two"
        in cart_with_product.current_url
    ), "User not navigated to checkout overview page"

    # Step 6:
    # Validate product still exists

    assert (
        len(cart_page.get_cart_items()) == 1
    ), "Product missing in checkout overview page"

    # Step 7:
    # Complete checkout

    checkout_page.click_finish()

    # Step 8:
    # Validate completion page

    assert (
        "checkout-complete"
        in cart_with_product.current_url
    ), "User not navigated to checkout completion page"

    # Step 9:
    # Validate success message

    assert (
        checkout_page.get_confirmation_message()
        == "Thank you for your order!"
    ), "Order confirmation message mismatch"