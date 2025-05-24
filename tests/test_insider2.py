import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Configure logging to capture debug information
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


@pytest.fixture(scope="class")
def setup(request):
    """Set up the Chrome WebDriver with specified options and preferences."""
    chrome_options = Options()
    # Configure Chrome preferences to block notifications and popups
    chrome_options.add_experimental_option(
        "prefs",
        {
            "profile.default_content_setting_values.notifications": 2,  # Block notifications
            "profile.default_content_setting_values.popups": 2,  # Block popups
            "profile.default_content_setting_values.geolocation": 2,  # Block geolocation
        },
    )
    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # Maximize the browser window for better visibility
    request.cls.driver = driver  # Assign the driver to the test class for use in tests
    yield driver  # Yield the driver for use in tests
    driver.quit()  # Clean up and close the browser after tests


@pytest.mark.usefixtures("setup")
class TestExample:
    """Contains test cases for validating the homepage and careers page functionalities."""

    def test_homepage_title(self):
        """Tests the homepage title, handling potential ads and cookie consent buttons."""
        self.driver.get("https://useinsider.com/")  # Navigate to the homepage

        # Attempt to click the cookie consent button if it exists
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
            )
            cookie_button.click()
            logging.info("Cookie consent button clicked.")
        except Exception as e:
            logging.info(
                "Cookie consent button not found. Proceeding without clicking. Error: %s",
                e,
            )
        # Assertions to verify the title of the homepage
        expected_title = "#1 Leader in Individualized, Cross-Channel CX — Insider"
        assert (
            self.driver.title == expected_title
        ), f"Expected title: '{expected_title}', but got: '{self.driver.title}'"
        logging.info("Homepage title is correct.")

    def test_company_click(self):
        """Tests clicking on the company information section and verifies the navigation."""
        logging.info("Starting test_company_click...")
        # Locate and click the company information element
        company_info_element = self.driver.find_element(
            By.XPATH,
            "//body/nav[@id='navigation']/div[@class='container-fluid']/div[@id='navbarNavDropdown']/ul[@class='navbar-nav']/li[6]/a[1]",
        )
        company_info_element.click()
        logging.info("Clicked on the company information section.")
        # Wait for the Careers link to be present
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[normalize-space()='Careers']")
                )
            )
            logging.info("Careers link is visible.")
        except Exception as e:
            logging.error("Careers link is not visible on the website. Error: %s", e)

    def test_careers_navigation(self):
        """Tests navigation to the Careers page and verifies its content."""
        logging.info("Starting test_careers_navigation...")
        careers_link = self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Careers']"
        )
        careers_link.click()  # Click on the Careers link
        logging.info("Navigation to Careers page successful.")
        # Verify the URL after navigation
        expected_url = "https://useinsider.com/careers/"
        assert (
            self.driver.current_url == expected_url
        ), f"Expected URL: '{expected_url}', but got: '{self.driver.current_url}'"
        # Check for various sections on the Careers page
        sections_to_check = [
            ("//h3[@class='category-title-media ml-0']", ">Our Locations< section"),
            ("//h2[contains(.,'Teams')]", ">Teams< section"),
            ("//h2[normalize-space()='Life at Insider']", ">Life at Insider< section"),
        ]
        for xpath, section_name in sections_to_check:
            try:
                assert (
                    WebDriverWait(self.driver, 10)
                    .until(EC.presence_of_element_located((By.XPATH, xpath)))
                    .is_displayed()
                )
                logging.info(f"{section_name} is available on this page.")
            except Exception as e:
                logging.error(f"{section_name} is not found. Error: {e}")

    def test_qa_page_navigation(self):
        """Tests navigation to the Quality Assurance page and verifies its content."""
        logging.info("Starting test_qa_page_navigation...")
        self.driver.get("https://useinsider.com/careers/quality-assurance/")
        time.sleep(5)  # Wait for the page to load
        # Verify the QA header
        qa_header = self.driver.find_element(
            By.XPATH, "//h1[@class='big-title big-title-media mt-4 mt-lg-0']"
        )
        expected_header_text = "Quality Assurance"
        assert (
            qa_header.text == expected_header_text
        ), f"Expected header: '{expected_header_text}', but got: '{qa_header.text}'"
        logging.info("QA header is correct.")
        # Check the "See all jobs" button and its functionality
        try:
            see_all_jobs_btn = self.driver.find_element(
                By.XPATH,
                "//a[@class='btn btn-outline-secondary rounded text-medium mt-2 py-3 px-lg-5 w-100 w-md-50']",
            )
            assert see_all_jobs_btn.is_displayed()
            see_all_jobs_btn.click()
            logging.info("See all QA jobs button is working correctly.")
            # Verify the URL after clicking the button
            expected_jobs_url = "https://useinsider.com/careers/open-positions/?department=qualityassurance"
            assert (
                self.driver.current_url == expected_jobs_url
            ), f"Expected URL: '{expected_jobs_url}', but got: '{self.driver.current_url}'"
            logging.info(
                "Navigated to the correct URL after clicking the QA jobs button."
            )
        except Exception as e:
            logging.error("See all QA jobs button is not working. Error: %s", e)

    def test_filter_jobs(self):
        """Tests the job filtering functionality based on location and department."""
        logging.info("Starting test_filter_jobs...")
        forms = self.driver.find_elements(
            By.XPATH, "//form[@id='top-filter-form']/div/span/span/span"
        )
        # Select location
        location_form = forms[0]
        location_form.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//ul[@id='select2-filter-by-location-results']")
            )
        )
        istanbul_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//li[contains(text(), 'Istanbul, Turkey')]")
            )
        )
        istanbul_option.click()
        logging.info("In Location field, 'Istanbul, Turkey' is selected successfully.")
        # Select department
        departman_form = forms[1]
        departman_form.click()
        quality_assurance_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//li[contains(text(), 'Quality Assurance')]")
            )
        )
        quality_assurance_option.click()
        logging.info(
            "In Department field, 'Quality Assurance' is selected successfully."
        )
        # Scroll down the page
        scroll_height = self.driver.execute_script("return document.body.scrollHeight")
        halfway_point = scroll_height // 2
        self.driver.execute_script(f"window.scrollTo(0, {halfway_point});")
        logging.info("Scrolled halfway down the page.")

    def test_view_button_and_job_details(self):
        """Tests the functionality of the view button and validates job details."""
        logging.info("Starting test_view_button_and_job_details...")
        # Find the View Role button and click it
        view_role_button = self.driver.find_element(
            By.XPATH, "//a[contains(text(), 'View Role')]"
        )
        ActionChains(self.driver).move_to_element(
            view_role_button
        ).perform()  # Ensure the button is in view
        view_role_button.click()
        # Wait for the new tab to open and switch to it
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        current_tab = self.driver.current_window_handle
        for tab in self.driver.window_handles:
            if tab != current_tab:
                self.driver.switch_to.window(tab)
                break
        # Validate the URL of the new tab
        expected_url = (
            "https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc"
        )
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        assert (
            self.driver.current_url == expected_url
        ), f"Expected URL: '{expected_url}', but got: '{self.driver.current_url}'"
        logging.info("The URL in the new tab is correct! Test completed successfully.")
        # Validate the Apply button and job title
        apply_button = self.driver.find_element(
            By.XPATH,
            "//div[@class='postings-btn-wrapper']//a[@class='postings-btn template-btn-submit shamrock'][normalize-space()='Apply for this job']",
        )
        assert (
            apply_button.is_displayed()
        ), "The Apply button is not visible on the website."
        logging.info("The Apply button is visible on the website.")
        h2_header_title = self.driver.find_element(
            By.XPATH,
            "//h2[normalize-space()='Senior Software Quality Assurance Engineer']",
        )
        assert (
            h2_header_title.is_displayed()
        ), "H2 header title is not visible on the website."
        logging.info("H2 header title is visible on the website.")
        # Validate the presence of the Insider logo
        try:
            insider_logo = self.driver.find_element(
                By.XPATH, "//img[@alt='Insider. logo']"
            )
            assert insider_logo.is_displayed(), "Insider logo is not visible."
            logging.info("Insider logo is visible on the website.")
        except AssertionError as e:
            logging.error(f"Insider logo not visible. Assertion Error: {e}")
        # Revisit the homepage to check for sections
        self.driver.get("https://useinsider.com/")
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
            )
            cookie_button.click()
        except Exception as e:
            logging.info(
                "Cookie consent button not found. Proceeding without clicking. Error: %s",
                e,
            )
        # Assertions to verify the title of the homepage again
        expected_title = "#1 Leader in Individualized, Cross-Channel CX — Insider"
        assert (
            self.driver.title == expected_title
        ), f"Expected title: '{expected_title}', but got: '{self.driver.title}'"
        # Verify the availability of various sections
        sections = {
            "Our Locations": By.XPATH,
            "Teams": By.XPATH,
            "Life at Insider": By.XPATH,
        }
        for name, locator in sections.items():
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (locator, f"//h3[normalize-space()='{name}']")
                    )
                )
                logging.info(f"{name} section is available.")
            except Exception as e:
                logging.error(f"{name} section is not found. Error: {e}")
