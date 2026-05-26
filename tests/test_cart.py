from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_product_visible_in_cart(
        cart_with_product
):

    inventory_page = InventoryPage(
        cart_with_product
    )

    inventory_page.open_cart()

    cart_page = CartPage(
        cart_with_product
    )

    assert (
        len(cart_page.get_cart_items()) == 1
    ), "Product not visible in cart"


def test_remove_product_from_cart(
        cart_with_product
):

    inventory_page = InventoryPage(
        cart_with_product
    )

    inventory_page.open_cart()

    cart_page = CartPage(
        cart_with_product
    )

    cart_page.remove_product()

    assert (
        len(cart_page.get_cart_items()) == 0
    ), "Product was not removed from cart"


def test_checkout_button_navigation(
        cart_with_product
):

    inventory_page = InventoryPage(
        cart_with_product
    )

    inventory_page.open_cart()

    cart_page = CartPage(
        cart_with_product
    )

    cart_page.click_checkout()

    assert (
        "checkout-step-one"
        in cart_with_product.current_url
    ), "User not navigated to checkout information page"


def test_continue_shopping_navigation(
        cart_with_product
):

    inventory_page = InventoryPage(
        cart_with_product
    )

    inventory_page.open_cart()

    cart_page = CartPage(
        cart_with_product
    )

    cart_page.click_continue_shopping()

    assert (
        "inventory"
        in cart_with_product.current_url
    ), "User not navigated back to inventory page"


def test_cart_page_title(
        cart_with_product
):

    inventory_page = InventoryPage(
        cart_with_product
    )

    inventory_page.open_cart()

    cart_page = CartPage(
        cart_with_product
    )

    assert (
        cart_page.get_cart_title()
        == "Your Cart"
    ), "Cart page title mismatch"