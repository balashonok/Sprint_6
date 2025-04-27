import allure

from pages.base_page import BasePage
from locators.main_page_locators import OrderLocators
from locators.transition_locators import TransitionLocators

class TransitionPage(BasePage):

    @allure.step('Клик на кнопку "Заказать"')
    def click_to_order(self):
        self.click_to_element(OrderLocators.HEADER_ORDER)

    @allure.step('Клик на лого "Самокат"')
    def click_to_logo(self):
        self.click_to_element_with_wait(TransitionLocators.LOGO)

    @allure.step('Клик на лого "Яндекс"')
    def click_to_yandex(self):
        self.click_to_element_with_wait(TransitionLocators.YANDEX_LOGO)

    @allure.step('Проверка редиректа на "Яндекс Дзен"')
    def check_redirect_dzen(self):
        self.switch_to_new_window()
        self.wait_title('Дзен')

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        self.get_url()