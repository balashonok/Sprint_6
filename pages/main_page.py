import allure

from conftests import firefox
from locators.main_page_locators import MainPageLocators
from locators.main_page_locators import OrderLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATORS, num)
        self.wait_and_scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element_with_wait(locator_q_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATORS, num)
        return self.get_text_from_element(locator_a_formatted)

    def click_order_hat(self, firefox):
        # WebDriverWait(firefox, 3).until(expected_conditions.element_to_be_clickable(OrderLocators.HEADER_ORDER))
        firefox.find_element(*OrderLocators.HEADER_ORDER).click()

    def click_order_bottom(self, firefox):
        # WebDriverWait(firefox, 3).until(expected_conditions.element_to_be_clickable(OrderLocators.HEADER_ORDER))
        firefox.find_element(*OrderLocators.BOTTOM_ORDER).click()
