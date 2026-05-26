from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import get_logger


class LoginPage(BasePage):

    logger = get_logger()

    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):

        super().__init__(driver)

    def enter_username(self, username):

        self.logger.info(f"Entering username: {username}")

        self.enter_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):

        self.logger.info("Entering password")

        self.enter_text(self.PASSWORD_FIELD, password)

    def click_login(self):

        self.logger.info("Clicking login button")

        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):

        self.logger.info("Starting login process")

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):

        error_message = self.get_text(self.ERROR_MESSAGE)

        self.logger.error(
            f"Login failed with error: {error_message}"
        )

        return error_message