import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from locators.main_page_locators import AcceptCookieLocators

from data.urls import URLs

@pytest.fixture()
def firefox():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox()
    driver.get(URLs.MAIN_PAGE)
    driver.find_element(*AcceptCookieLocators.ACCEPT_COOKIE_BUTTON).click()
    yield driver
    driver.quit()
