from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import get_logger


class CartPage(BasePage):

    logger = get_logger()

    CART_ITEMS = (
        By.CLASS_NAME,
        "cart_item"
    )

    REMOVE_BUTTON = (
        By.ID,
        "remove-sauce-labs-backpack"
    )

    CHECKOUT_BUTTON = (
        By.ID,
        "checkout"
    )

    CONTINUE_SHOPPING_BUTTON = (
        By.ID,
        "continue-shopping"
    )

    CART_TITLE = (
        By.CLASS_NAME,
        "title"
    )

    def __init__(self, driver):

        super().__init__(driver)

    def get_cart_items(self):

        items = self.driver.find_elements(
            *self.CART_ITEMS
        )

        self.logger.info(
            f"Total cart items: {len(items)}"
        )

        return items

    def remove_product(self):

        self.logger.info(
            "Removing product from cart"
        )

        self.click(self.REMOVE_BUTTON)

    def click_checkout(self):

        self.logger.info(
            "Clicking checkout button"
        )

        self.click(self.CHECKOUT_BUTTON)

    def click_continue_shopping(self):

        self.logger.info(
            "Clicking continue shopping button"
        )

        self.click(
            self.CONTINUE_SHOPPING_BUTTON
        )

    def get_cart_title(self):

        title = self.get_text(
            self.CART_TITLE
        )

        self.logger.info(
            f"Cart page title: {title}"
        )

        return title