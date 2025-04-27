import allure

from conftests import firefox
from pages.transition_page import TransitionPage
from data.urls import URLs


class TestTransition:

    @allure.title('Проверка перехода на "Дзен"')
    def test_transition_yandex(self, firefox):
        page = TransitionPage(firefox)
        page.click_to_yandex()
        page.check_redirect_dzen()
        assert firefox.current_url == URLs.YANDEX

    @allure.title('Проверка перехода на лого "Самокат"')
    def test_transition_scooter(self, firefox):
        page = TransitionPage(firefox)
        page.click_to_order()
        page.click_to_logo()
        assert firefox.current_url == URLs.MAIN_PAGE
