from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import get_logger


class CheckoutPage(BasePage):

    logger = get_logger()

    FIRST_NAME_FIELD = (
        By.ID,
        "first-name"
    )

    LAST_NAME_FIELD = (
        By.ID,
        "last-name"
    )

    POSTAL_CODE_FIELD = (
        By.ID,
        "postal-code"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    FINISH_BUTTON = (
        By.ID,
        "finish"
    )

    COMPLETE_HEADER = (
        By.CLASS_NAME,
        "complete-header"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "h3[data-test='error']"
    )

    def __init__(self, driver):

        super().__init__(driver)

    def enter_first_name(self, first_name):

        self.logger.info(
            f"Entering first name: {first_name}"
        )

        self.enter_text(
            self.FIRST_NAME_FIELD,
            first_name
        )

    def enter_last_name(self, last_name):

        self.logger.info(
            f"Entering last name: {last_name}"
        )

        self.enter_text(
            self.LAST_NAME_FIELD,
            last_name
        )

    def enter_postal_code(self, postal_code):

        self.logger.info(
            f"Entering postal code: {postal_code}"
        )

        self.enter_text(
            self.POSTAL_CODE_FIELD,
            postal_code
        )

    def click_continue(self):

        self.logger.info(
            "Clicking continue button"
        )

        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):

        self.logger.info(
            "Clicking finish button"
        )

        self.click(self.FINISH_BUTTON)

    def complete_checkout(
            self,
            first_name,
            last_name,
            postal_code
    ):

        self.enter_first_name(first_name)

        self.enter_last_name(last_name)

        self.enter_postal_code(postal_code)

        self.click_continue()

    def get_confirmation_message(self):

        message = self.get_text(
            self.COMPLETE_HEADER
        )

        self.logger.info(
            f"Order confirmation message: "
            f"{message}"
        )

        return message

    def get_error_message(self):

        error = self.get_text(
            self.ERROR_MESSAGE
        )

        self.logger.error(
            f"Checkout error message: {error}"
        )

        return error