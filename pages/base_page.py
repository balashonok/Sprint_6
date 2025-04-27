from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from conftests import firefox

class BasePage:
    TIMEOUT = 3

    def __init__(self, firefox):
        self.firefox = firefox
        self.wait = WebDriverWait(firefox, self.TIMEOUT)

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_element_with_wait(self, locator):
        self.wait_for_element(locator)
        return self.firefox.find_element(*locator)

    def is_displayed(self, locator):
        self.wait_for_element(locator)
        return self.firefox.find_element(*locator).is_displayed()

    def click_to_element_with_wait(self, locator):
        self.wait_for_clickable(locator)
        self.firefox.find_element(*locator).click()

    def click_to_element(self, locator):
        self.firefox.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def _scroll_to_element(self, element):
        self.firefox.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def wait_and_scroll_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return self._scroll_to_element(element)

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    def switch_to_new_window(self):
        original_window = self.firefox.current_window_handle
        self.wait.until(EC.number_of_windows_to_be(2))
        for window in self.firefox.window_handles:
            if window != original_window:
                self.firefox.switch_to.window(window)
                return window

    def wait_title(self, expected_title):
        return self.wait.until(EC.title_contains(expected_title))

    def get_url(self):
        return self.firefox.current_url
