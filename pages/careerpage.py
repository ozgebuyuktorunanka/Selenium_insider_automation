import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from tests.test_insider import setup

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


class CareersPage(object):
    def __init__(self, page):
        self.page = page
        self.driver = setup()

    def test_careers_navigation(self):
        logging.info("Starting test_careers_navigation...")
        try:
            careers_link = self.driver.find_element(
                By.XPATH, "//a[normalize-space()='Careers']"
            )
            careers_link.click()
            logging.info("Clicked on Careers link.")
            assert self.driver.current_url == "https://useinsider.com/careers/"
            logging.info("Navigated to the correct Careers URL.")
        except AssertionError:
            logging.error("Failed to navigate to the correct Careers URL.")

        try:
            assert WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//h3[@class='category-title-media ml-0']")
                )
            )
            logging.info(">Life at >Our Locations< section is available on this page.")
        except Exception as e:
            logging.error(
                f"There is no >Our Locations< section on this page. Error: {e}"
            )
        try:
            assert self.driver.find_element(
                By.XPATH, "//h2[contains(.,'Teams')]"
            ).is_displayed()
            logging.info(">Life at >Teams< section is available on this page.")
        except Exception as e:
            logging.error(f"There is no >Teams< section on this page. Error: {e}")
        try:
            assert self.driver.find_element(
                By.XPATH, "//h2[normalize-space()='Life at Insider']"
            ).is_displayed()
            logging.info(">Life at >Insider< section is available on this page.")
        except Exception as e:
            logging.error(
                f"There is no >Life at Insider< section on this page. Error: {e}"
            )

    def test_qa_page_navigation(self):
        logging.info("Starting test_qa_page_navigation...")
        self.driver.get("https://useinsider.com/careers/quality-assurance/")
        try:
            qa_header = self.driver.find_element(
                By.XPATH, "//h1[@class='big-title big-title-media mt-4 mt-lg-0']"
            )
            assert qa_header.text == "Quality Assurance"
            logging.info("QA header is equal to >Quality Assurance< text.")
        except AssertionError:
            logging.error("QA header is not equal to >Quality Assurance< text.")

        try:
            see_all_jobs_btn = self.driver.find_element(
                By.XPATH,
                "//a[@class='btn btn-outline-secondary rounded text-medium mt-2 py-3 px-lg-5 w-100 w-md-50']",
            )
            assert see_all_jobs_btn.is_displayed()
            see_all_jobs_btn.click()
            logging.info("See all QA jobs button is working correctly.")
        except Exception as e:
            logging.error(f"See all QA jobs button is not working. Error: {e}")
        try:
            assert (
                self.driver.current_url
                == "https://useinsider.com/careers/open-positions/?department=qualityassurance"
            )
            logging.info("After clicking QA jobs button - navigated URL is correct.")
        except AssertionError:
            logging.error(
                "After clicking QA jobs button - navigated URL is not correct."
            )
        time.sleep(5)

    def test_filter_jobs(self):
        logging.info("Starting test_filter_jobs...")
        try:
            forms = self.driver.find_elements(
                By.XPATH, "//form[@id='top-filter-form']/div/span/span/span"
            )
            location_form = forms[0]
            location_form.click()
            logging.info("Clicked on location filter.")
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
            logging.info(
                "In Location field, >Istanbul Turkey< is selected successfully."
            )
        except Exception as e:
            logging.error(f"Failed to select Istanbul in location filter. Error: {e}")
        try:
            departman_form = forms[1]
            departman_form.click()
            quality_assurance_option = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//li[contains(text(), 'Quality Assurance')]")
                )
            )
            quality_assurance_option.click()
            logging.info(
                "In Department field, >Quality Assurance< is selected successfully."
            )
        except Exception as e:
            logging.error(
                f"Failed to select Quality Assurance in department filter. Error: {e}"
            )
        time.sleep(2)
        scroll_height = self.driver.execute_script("return document.body.scrollHeight")
        halfway_point = scroll_height // 3
        self.driver.execute_script(f"window.scrollTo(0, {halfway_point});")
        logging.info("Scrolled halfway down the page.")

    def test_view_button_and_job_details(self):
        logging.info("Starting test_view_button_and_job_details...")
        try:
            view_role_button = self.driver.find_element(
                By.XPATH, "//a[contains(text(), 'View Role')]"
            )
            action = ActionChains(self.driver)
            action.move_to_element(view_role_button).perform()
            view_role_button.click()
            logging.info("Clicked on View Role button.")
        except Exception as e:
            logging.error(f"Failed to click on View Role button. Error: {e}")
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        current_tab = self.driver.current_window_handle
        all_tabs = self.driver.window_handles
        for tab in all_tabs:
            if tab != current_tab:
                self.driver.switch_to.window(tab)
                break
        expected_url = (
            "https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc"
        )
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        current_url = self.driver.current_url
        try:
            assert current_url == expected_url
            logging.info(
                "The URL in the new tab is correct! Test completed successfully."
            )
        except AssertionError:
            logging.error("The URL in the new tab is incorrect.")
        try:
            apply_button = self.driver.find_element(
                By.XPATH,
                "//div[@class='postings-btn-wrapper']//a[@class='postings-btn template-btn-submit shamrock'][normalize-space()='Apply for this job']",
            )
            assert apply_button.is_displayed()
            logging.info("The Apply button is visible on the website.")
        except Exception as e:
            logging.error(f"The Apply button is not visible. Error: {e}")
        time.sleep(5)
        try:
            h2_header_title = self.driver.find_element(
                By.XPATH,
                "//h2[normalize-space()='Senior Software Quality Assurance Engineer']",
            )
            assert h2_header_title.is_displayed()
            logging.info("H2 header title is visible on the website.")
        except Exception as e:
            logging.error(f"H2 header title is not visible. Error: {e}")
        try:
            insider_logo = self.driver.find_element(
                By.XPATH, "//img[@alt='Insider. logo']"
            )
            assert insider_logo.is_displayed()
            logging.info("Insider logo is visible on the website.")
        except AssertionError as e:
            logging.error(f"Insider logo not visible - Assertion Error: {e}")
        self.driver.get("https://useinsider.com/")
        try:
            self.driver.find_element(By.ID, "wt-cli-accept-all-btn").click()
            logging.info("Clicked cookie consent button.")
        except Exception as e:
            logging.error(f"Failed to click cookie consent button. Error: {e}")
        try:
            assert (
                self.driver.title
                == "#1 Leader in Individualized, Cross-Channel CX — Insider"
            )
            logging.info("Page title is correct.")
        except AssertionError:
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
                logging.info(f"{name} section is available.")
            except Exception as e:
                logging.error(f"{name} section is not found. Error: {e}")
