import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.screenshot_utils import take_screenshot
from config import (
    BASE_URL,
    IMPLICIT_WAIT,
    HEADLESS
)



@pytest.fixture(scope="function")
def driver():

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--no-sandbox")

    chrome_options.add_argument(
        "--disable-dev-shm-usage"
    )

    chrome_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
    )
    if HEADLESS:

        chrome_options.add_argument(
            "--headless=new"
        )

    chrome_options.add_argument(
        "--disable-notifications"
    )

    chrome_options.add_argument(
        "--disable-popup-blocking"
    )

    chrome_options.add_argument(
        "--disable-infobars"
    )

    chrome_options.add_argument(
        "--guest"
    )

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=chrome_options
    )

    driver.maximize_window()

    driver.implicitly_wait(IMPLICIT_WAIT)

    driver.get(BASE_URL)


    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver):

    login_page = LoginPage(driver)

    login_page.login(
        username="standard_user",
        password="secret_sauce"
    )

    return driver


@pytest.fixture(scope="function")
def cart_with_product(logged_in_driver):

    inventory_page = InventoryPage(
        logged_in_driver
    )

    inventory_page.add_backpack_to_cart()

    return logged_in_driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            screenshot_path = take_screenshot(
                driver,
                item.name
            )

            print(
                f"\nScreenshot saved at: "
                f"{screenshot_path}"
            )
from pages.cart_page import CartPage


@pytest.fixture(scope="function")
def checkout_page_setup(cart_with_product):

    inventory_page = InventoryPage(
        cart_with_product
    )

    inventory_page.open_cart()

    cart_page = CartPage(
        cart_with_product
    )

    cart_page.click_checkout()

    return cart_with_product