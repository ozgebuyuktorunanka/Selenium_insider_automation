<<<<<<< HEAD
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.test_insider import setup

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class HomePage(object):
    def __init__(self, page):
        self.page = page
        self.driver = setup()
        
    def test_homepage_title(self):
        
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

    def test_company_click(self):
        self.driver.find_element(
            By.XPATH,
            "//body/nav[@id='navigation']/div[@class='container-fluid']/div[@id='navbarNavDropdown']/ul[@class='navbar-nav']/li[6]/a[1]",
        ).click()

        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[normalize-space()='Careers']")
            )
=======
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        try:
            cookie_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
            )
            cookie_btn.click()
        except:
            pass  # Button may not be visible

    def go_to_homepage(self):
        self.driver.get("https://useinsider.com/")

    def get_title(self):
        return self.driver.title

    def click_company_tab(self):
        company_tab = self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Company' or contains(text(),'Company')]"
        )
        company_tab.click()

    def is_careers_link_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Careers']"))
>>>>>>> a511a1b (some refactoring activities)
        )
