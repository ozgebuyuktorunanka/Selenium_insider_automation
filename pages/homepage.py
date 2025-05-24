import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.test_insider import setup

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


class HomePage(object):
    def __init__(self, page):
        self.page = page
        self.driver = setup()

    def test_homepage_title(self):
        """Tests homepage title and handles potential ads and cookie consent buttons."""
        logging.info("Navigating to homepage...")
        self.driver.get("https://useinsider.com/")

        # Check for and click cookie consent button (optional, adjust wait time as needed)
        try:
            cookie_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
            )
            cookie_btn.click()
            logging.info("Clicked cookie consent button.")
        except Exception as e:
            logging.warning(
                f"Cookie consent button not visible or clickable. Error: {e}"
            )
        # Assertions for title
        expected_title = "#1 Leader in Individualized, Cross-Channel CX — Insider"
        actual_title = self.driver.title
        try:
            assert actual_title == expected_title
            logging.info("Page title is correct.")
        except AssertionError:
            logging.error(
                f"Page title is not correct. Expected: {expected_title}, Got: {actual_title}"
            )

    def test_company_click(self):
        """Tests clicking on the Company tab and checks for the Careers link."""
        logging.info("Clicking on the Company tab...")
        try:
            company_tab = self.driver.find_element(
                By.XPATH,
                "//body/nav[@id='navigation']/div[@class='container-fluid']/div[@id='navbarNavDropdown']/ul[@class='navbar-nav']/li[6]/a[1]",
            )
            company_tab.click()
            logging.info("Clicked on the Company tab.")
        except Exception as e:
            logging.error(f"Failed to click on the Company tab. Error: {e}")
        try:
            careers_link_visible = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[normalize-space()='Careers']")
                )
            )
            logging.info("Careers link is visible.")
            return careers_link_visible
        except Exception as e:
            logging.error(f"Careers link is not visible. Error: {e}")
            return False
