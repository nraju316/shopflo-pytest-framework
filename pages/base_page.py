from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):

        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()



    def enter_text(self, locator, text):

        if text is None:

            text = ""

        elif isinstance(text, float):

            if math.isnan(text):

                text = ""

            else:

                text = str(int(text))

        else:

            text = str(text)

        self.wait.until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def get_text(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text