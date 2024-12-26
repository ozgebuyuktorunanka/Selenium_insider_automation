import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from tests.test_insider import setup

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

class CareersPage(object):
    def __init__(self, page):
        self.page = page
        self.driver = setup()
         
    def test_careers_navigation(self):
        careers_link = self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Careers']"
        )
        careers_link.click()

        assert self.driver.current_url == "https://useinsider.com/careers/"

        try:
            assert WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//h3[@class='category-title-media ml-0']")
                )
            )  # Our Locations Section Control
            logging.info(">Life at >Our Locations< section is avaible on this page.")
        except:
            logging.error("There is no >Our Locations< section on this page.")

        try:
            assert self.driver.find_element(
                By.XPATH, "//h2[contains(.,'Teams')]"  # Teams Section Control
            ).is_displayed()
            logging.info(">Life at >Teams< section is avaible on this page.")
        except:
            logging.error("There is no >Teams< section on this page.")

        try:
            assert self.driver.find_element(
                By.XPATH,
                "//h2[normalize-space()='Life at Insider']",  # Life at Insider Section Control
            ).is_displayed()
            logging.info(">Life at >Insider< section is avaible on this page.")
        except:
            logging.error("There is no >Life at Insider< section on this page.")

    def test_qa_page_navigation(self):
        self.driver.get("https://useinsider.com/careers/quality-assurance/")

        # Quality Assurance header and innerText Control
        qa_header = self.driver.find_element(
            By.XPATH, "//h1[@class='big-title big-title-media mt-4 mt-lg-0']"
        )
        try:
            assert qa_header.text == "Quality Assurance"
            logging.info("QA header is equal with >Quality Assurance< text.")
        except:
            logging.error("QA header is not equal with >Quality Assurance< text.")

        try:
            see_all_jobs_btn = self.driver.find_element(
                By.XPATH,
                "//a[@class='btn btn-outline-secondary rounded text-medium mt-2 py-3 px-lg-5 w-100 w-md-50']",
            )
            assert see_all_jobs_btn.is_displayed()
            see_all_jobs_btn.click()
            logging.info("See all QA jobs button is working correctly.")
        except:
            logging.error("See all QA jobs button is not working.")

        try:
            assert (
                self.driver.current_url
                == "https://useinsider.com/careers/open-positions/?department=qualityassurance"
            )
            logging.info("After clicking QA jobs button - navigated URL is correct.")
        except:
            logging.error(
                "After clicking QA jobs button - navigated URL is not correct."
            )
        time.sleep(5)

    def test_filter_jobs(self):
        forms = self.driver.find_elements(
            By.XPATH, "//form[@id='top-filter-form']/div/span/span/span"
        )
        location_form = forms[0]
        location_form.click()

        # Wait for list loading
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
        logging.info("In Location field,>Istanbul Turkey< is selected succesfully.")

        departman_form = forms[1]
        departman_form.click()

        quality_assurance_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//li[contains(text(), 'Quality Assurance')]")
            )
        )
        quality_assurance_option.click()
        time.sleep(2)

        # Scroll halfway down the page
        scroll_height = self.driver.execute_script(
            "return document.body.scrollHeight"
        )  # Get total page height
        halfway_point = scroll_height // 3

        # Scroll to halfway point
        self.driver.execute_script(f"window.scrollTo(0, {halfway_point});")

    def test_view_button_and_job_details(self):
        # Find the element (View Role button)
        view_role_button = self.driver.find_element(
            By.XPATH, "//a[contains(text(), 'View Role')]"
        )

        # Create an ActionChains object
        action = ActionChains(self.driver)

        # Move to the element to make it visible
        action.move_to_element(view_role_button).perform()

        # Click the element after making it visible
        view_role_button.click()

        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )  # Wait until the new tab opens

        # Get references of existing tabs
        current_tab = self.driver.current_window_handle
        all_tabs = self.driver.window_handles

        # Switch the new tab.
        for tab in all_tabs:
            if tab != current_tab:
                self.driver.switch_to.window(tab)
                break

        expected_url = (
            "https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc"
        )
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        current_url = self.driver.current_url
        assert current_url == expected_url

        logging.info("The URL in the new tab is correct! Test completed successfully.")

        apply_button = self.driver.find_element(
            By.XPATH,
            "//div[@class='postings-btn-wrapper']//a[@class='postings-btn template-btn-submit shamrock'][normalize-space()='Apply for this job']",
        )
        assert apply_button.is_displayed()
        logging.info("The Apply button is visible in website.")
        time.sleep(5)

        h2_header_title = self.driver.find_element(
            By.XPATH,
            "//h2[normalize-space()='Senior Software Quality Assurance Engineer']",
        )
        assert h2_header_title.is_displayed()
        logging.info("H2 header title is visible on website.")

        try:
            insider_logo = self.driver.find_element(
                By.XPATH, "//img[@alt='Insider. logo']"
            )
            assert insider_logo.is_displayed()
            logging.info("Insider logo is visible in website.")

        except AssertionError as e:
            logging.error(f"Insider logo not visible-Assertion Error:{e}")

        """Tests homepage title and handles potential ads and cookie consent buttons."""
        self.driver.get("https://useinsider.com/")

        # Check for and click cookie consent button (optional, adjust wait time as needed)
        self.driver.find_element(By.ID, "wt-cli-accept-all-btn").click()

        # Assertions
        try:
            assert (
                self.driver.title
                == "#1 Leader in Individualized, Cross-Channel CX — Insider"
            )
        except:
            logging.error("Page title is not correct.")

        sections = {
            "Our Locations": By.XPATH,
            "Teams": By.XPATH,
            "Life at Insider": By.XPATH,
        }
        for name, locator in sections.items():
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(locator)
                )
                print(f"{name} section is available")
            except:
                print(f"{name} section is not found")
