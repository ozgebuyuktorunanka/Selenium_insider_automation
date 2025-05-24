import logging
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.careerpage import CareersPage
from pages.homepage import HomePage

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


@pytest.fixture()
def setup(request):
    """Set up the Chrome WebDriver with specified options and preferences."""
    chrome_options = Options()
    # Configure Chrome preferences to block certain features
    prefs = {
        "profile.default_content_setting_values.notifications": 2,  # Block notifications
        "profile.default_content_setting_values.geolocation": 2,  # Block geolocation
        "profile.default_content_setting_values.camera": 2,  # Block camera access
        "profile.default_content_setting_values.microphone": 2,  # Block microphone access
    }
    chrome_options.add_experimental_option("prefs", prefs)
    # Add various arguments to enhance performance and security
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument(
        "--window-size=1920,1200"
    )  # Set the initial window size
    chrome_options.add_argument(
        "--ignore-certificate-errors"
    )  # Ignore SSL certificate errors
    chrome_options.add_argument("--disable-extensions")  # Disable browser extensions
    chrome_options.add_argument(
        "--no-sandbox"
    )  # Disable the sandbox for all process types
    chrome_options.add_argument(
        "--disable-dev-shm-usage"
    )  # Overcome limited resource problems in Docker
    # Initialize the WebDriver with the configured options
    driver = webdriver.Chrome(options=chrome_options)
    # Assign the driver to the test class for use in tests
    request.cls.driver = driver
    yield driver  # Yield the driver for use in tests
    # Teardown: Quit the driver after tests are completed
    logging.info("Quitting the WebDriver...")
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestExample:
    """Contains test cases for validating the homepage and careers page functionalities."""

    def test_homepage_title(self):
        """Tests the title of the homepage to ensure it displays correctly."""
        logging.info("Starting test_homepage_title...")
        self.homepage = HomePage(
            self.driver
        )  # Pass the driver to the HomePage instance
        expected_title = "#1 Leader in Individualized, Cross-Channel CX — Insider"
        actual_title = self.homepage.test_homepage_title()

        try:
            assert (
                actual_title == expected_title
            ), "Homepage title does not match expected."
            logging.info("Homepage title is correct.")
        except AssertionError as e:
            logging.error(f"Assertion Error: {e}")

    def test_company_click(self):
        """Tests clicking on the company information section."""
        logging.info("Starting test_company_click...")
        self.homepage = HomePage(
            self.driver
        )  # Pass the driver to the HomePage instance

        try:
            assert self.homepage.test_company_click(), "Failed to click on Company tab."
            logging.info("Company tab clicked successfully.")
        except AssertionError as e:
            logging.error(f"Assertion Error: {e}")

    def test_careers_navigation(self):
        """Tests navigation to the careers page to verify the link works."""
        logging.info("Starting test_careers_navigation...")
        self.careerpage = CareersPage(
            self.driver
        )  # Pass the driver to the CareersPage instance

        try:
            assert (
                self.careerpage.test_careers_navigation()
            ), "Failed to navigate to Careers page."
            logging.info("Successfully navigated to Careers page.")
        except AssertionError as e:
            logging.error(f"Assertion Error: {e}")

    def test_qa_page_navigation(self):
        """Tests navigation to the QA page from the careers page."""
        logging.info("Starting test_qa_page_navigation...")
        self.careerpage = CareersPage(
            self.driver
        )  # Pass the driver to the CareersPage instance

        try:
            assert (
                self.careerpage.test_qa_page_navigation()
            ), "Failed to navigate to QA page."
            logging.info("Successfully navigated to QA page.")
        except AssertionError as e:
            logging.error(f"Assertion Error: {e}")

    def test_filter_jobs(self):
        """Tests filtering job results based on specified criteria."""
        logging.info("Starting test_filter_jobs...")
        self.careerpage = CareersPage(
            self.driver
        )  # Pass the driver to the CareersPage instance

        try:
            assert (
                self.careerpage.test_filter_jobs()
            ), "Job filtering did not work as expected."
            logging.info("Job filtering works as intended.")
        except AssertionError as e:
            logging.error(f"Assertion Error: {e}")

    def test_view_button_and_job_details(self):
        """Tests the functionality of the view button and displays job details."""
        logging.info("Starting test_view_button_and_job_details...")
        self.careerpage = CareersPage(
            self.driver
        )  # Pass the driver to the CareersPage instance

        try:
            assert (
                self.careerpage.test_view_button_and_job_details()
            ), "Failed to view job details."
            logging.info("Job details displayed successfully.")
        except AssertionError as e:
            logging.error(f"Assertion Error: {e}")
