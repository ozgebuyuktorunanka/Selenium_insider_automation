import pytest
from selenium import webdriver
from pages.homepage import HomePage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_homepage_title(driver):
    homepage = HomePage(driver)
    homepage.go_to_homepage()
    homepage.accept_cookies()

    assert homepage.get_title() == "#1 Leader in Individualized, Cross-Channel CX — Insider", \
        "Homepage title does not match expected."

def test_company_tab_click(driver):
    homepage = HomePage(driver)
    homepage.go_to_homepage()
    homepage.accept_cookies()
    homepage.click_company_tab()

    assert homepage.is_careers_link_visible(), "Careers link is not visible after clicking Company."
