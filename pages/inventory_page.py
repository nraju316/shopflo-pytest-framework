from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import get_logger


class InventoryPage(BasePage):

    logger = get_logger()

    ADD_TO_CART_BACKPACK = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    REMOVE_BACKPACK = (
        By.ID,
        "remove-sauce-labs-backpack"
    )

    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    CART_ICON = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    PRODUCT_SORT = (
        By.CLASS_NAME,
        "product_sort_container"
    )

    INVENTORY_ITEMS = (
        By.CLASS_NAME,
        "inventory_item"
    )

    def __init__(self, driver):

        super().__init__(driver)

    def add_backpack_to_cart(self):

        self.logger.info(
            "Adding Sauce Labs Backpack to cart"
        )

        self.click(self.ADD_TO_CART_BACKPACK)

    def remove_backpack_from_cart(self):

        self.logger.info(
            "Removing Sauce Labs Backpack from cart"
        )

        self.click(self.REMOVE_BACKPACK)

    def get_cart_badge_count(self):

        badge_count = self.get_text(self.CART_BADGE)

        self.logger.info(
            f"Cart badge count is: {badge_count}"
        )

        return badge_count

    def open_cart(self):

        self.logger.info("Opening cart page")

        self.click(self.CART_ICON)

    def get_inventory_items(self):

        items = self.driver.find_elements(
            *self.INVENTORY_ITEMS
        )

        self.logger.info(
            f"Total inventory items displayed: {len(items)}"
        )

        return items