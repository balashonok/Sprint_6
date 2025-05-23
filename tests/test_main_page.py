import pytest
import allure

from conftests import firefox
from pages.main_page import MainPage
from data.main_page_answers import ANSWERS


class TestMainPage:

    @allure.title('Проверка выпадающих списков в разделе "Вопросы о важном"')
    @pytest.mark.parametrize('num, result', ANSWERS)
    def test_questions_and_answer(self, firefox, num, result):
        page = MainPage(firefox)
        page.click_to_question(num)
        assert page.get_answer_text(num) == result
