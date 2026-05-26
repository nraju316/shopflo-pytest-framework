from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def login(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )


def test_add_product_to_cart(driver):

    login(driver)

    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack_to_cart()

    assert (
        inventory_page.get_cart_badge_count() == "1"
    ), "Cart badge count mismatch after adding product"


def test_remove_product_from_cart(driver):

    login(driver)

    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack_to_cart()

    inventory_page.remove_backpack_from_cart()

    cart_items = driver.find_elements(
        *InventoryPage.CART_BADGE
    )

    assert (
        len(cart_items) == 0
    ), "Product was not removed from cart"


def test_inventory_products_displayed(driver):

    login(driver)

    inventory_page = InventoryPage(driver)

    products = inventory_page.get_inventory_items()

    assert (
        len(products) == 6
    ), "Inventory product count mismatch"