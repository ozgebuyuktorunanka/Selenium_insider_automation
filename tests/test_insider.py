import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.careerpage import CareersPage
from pages.homepage import HomePage
<<<<<<< HEAD

        
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
=======
@pytest.fixture()
def setup(request):
    """Set up the Chrome WebDriver with specified options and preferences."""
    chrome_options = Options()
    
    # Configure Chrome preferences to block certain features
    prefs = {
        "profile.default_content_setting_values.notifications": 2,  # Block notifications
        "profile.default_content_setting_values.geolocation": 2,  # Block geolocation
        "profile.default_content_setting_values.camera": 2,       # Block camera access
        "profile.default_content_setting_values.microphone": 2,   # Block microphone access
    }
    chrome_options.add_experimental_option("prefs", prefs)
    # Add various arguments to enhance performance and security
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument("--window-size=1920,1200")  # Set the initial window size
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors
    chrome_options.add_argument("--disable-extensions")  # Disable browser extensions
    chrome_options.add_argument("--no-sandbox")  # Disable the sandbox for all process types
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems in Docker
    # Initialize the WebDriver with the configured options
    driver = webdriver.Chrome(options=chrome_options)
    
    # Assign the driver to the test class for use in tests
    request.cls.driver = driver
    
    yield driver  # Yield the driver for use in tests
    
    # Teardown: Quit the driver after tests are completed
    driver.quit()
@pytest.mark.usefixtures("setup")
class TestExample:
    """Contains test cases for validating the homepage and careers page functionalities."""
    def test_homepage_title(self):
        """Tests the title of the homepage to ensure it displays correctly."""
        self.homepage = HomePage()
        assert self.homepage.test_homepage_title() == "Expected Title"  # Replace with the actual expected title
    def test_company_click(self):
        """Tests clicking on the company information section."""
        self.homepage = HomePage()
        assert self.homepage.test_company_click()  # Ensure the click action performs as expected
    def test_careers_navigation(self):
        """Tests navigation to the careers page to verify the link works."""
        self.careerpage = CareersPage()
        assert self.careerpage.test_careers_navigation()  # Validate that navigation is successful
    def test_qa_page_navigation(self):
        """Tests navigation to the QA page from the careers page."""
        self.careerpage = CareersPage()
        assert self.careerpage.test_qa_page_navigation()  # Ensure navigation to QA page is correct
    def test_filter_jobs(self):
        """Tests filtering job results based on specified criteria."""
        self.careerpage = CareersPage()
        assert self.careerpage.test_filter_jobs()  # Verify that job filtering works as intended
    def test_view_button_and_job_details(self):
        """Tests the functionality of the view button and displays job details."""
        self.careerpage = CareersPage()
        assert self.careerpage.test_view_button_and_job_details()  # Confirm that job details are displayed correctly
>>>>>>> a511a1b (some refactoring activities)
