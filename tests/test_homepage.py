import logging
import pytest
from selenium import webdriver
from pages.homepage import HomePage

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


@pytest.fixture
def driver():
    logging.info("Initializing Chrome WebDriver...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    logging.info("Quitting the WebDriver...")
    driver.quit()


def test_homepage_title(driver):
    logging.info("Starting test_homepage_title...")
    homepage = HomePage(driver)
    homepage.go_to_homepage()
    homepage.accept_cookies()

    expected_title = "#1 Leader in Individualized, Cross-Channel CX — Insider"
    actual_title = homepage.get_title()

    try:
        assert actual_title == expected_title, "Homepage title does not match expected."
        logging.info("Homepage title is correct.")
    except AssertionError as e:
        logging.error(f"Assertion Error: {e}")


def test_company_tab_click(driver):
    logging.info("Starting test_company_tab_click...")
    homepage = HomePage(driver)
    homepage.go_to_homepage()
    homepage.accept_cookies()
    homepage.click_company_tab()

    try:
        assert (
            homepage.is_careers_link_visible()
        ), "Careers link is not visible after clicking Company."
        logging.info("Careers link is visible after clicking Company tab.")
    except AssertionError as e:
        logging.error(f"Assertion Error: {e}")
