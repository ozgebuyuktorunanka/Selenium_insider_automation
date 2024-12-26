import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.careerpage import CareersPage
from pages.homepage import HomePage

        
@pytest.fixture()
def setup(request):
    chrome_options = Options()

    # Disable specific permissions (adjust as needed)
    prefs = {
        "profile.default_content_setting_values.notifications": 2,  # Block notifications
        "profile.default_content_setting_values.geolocation": 2,  # Block geolocation
        "profile.default_content_setting_values.camera": 2,       # Block camera
        "profile.default_content_setting_values.microphone": 2,  # Block microphone
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1200")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_homepage_title(self):
        """Tests the title of the homepage."""
        self.homepage = HomePage()
        self.homepage.test_homepage_title()

    def test_company_click(self):
        """Tests clicking on the company information section."""
        self.homepage = HomePage()
        self.homepage.test_company_click()

    def test_careers_navigation(self):
        """Tests navigation to the careers page."""
        self.careerpage = CareersPage()
        self.careerpage.test_careers_navigation()

    def test_qa_page_navigation(self):
        """Tests navigation to the QA page."""
        self.careerpage = CareersPage()
        self.careerpage.test_qa_page_navigation()

    def test_filter_jobs(self):
        """Tests filtering job results."""
        self.careerpage = CareersPage()
        self.careerpage.test_filter_jobs()

    def test_view_button_and_job_details(self):
        """Tests viewing job details."""
        # The line `selfcareerpage = CareersPage()` is attempting to create an instance of the
        # `CareersPage` class and assign it to the `selfcareerpage` variable. However, there seems to be a
        # typo in the code as it should be `self.careerpage = CareersPage()` instead of `selfcareerpage =
        # CareersPage()`.
        self.careerpage = CareersPage()
        self.careerpage.test_view_button_and_job_details()