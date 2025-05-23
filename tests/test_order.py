import allure
import pytest

from conftests import firefox
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA


class TestOrder:

    @allure.title('Проверка формирования заказа')
    @pytest.mark.parametrize("order_data", ORDER_DATA, ids=[order["name"] for order in ORDER_DATA])
    def test_order(self, firefox, order_data):
        page = OrderPage(firefox)
        page.click_to_order(order_data["button"])
        page.fill_in_name(order_data["name"])
        page.fill_in_surname(order_data["surname"])
        page.fill_in_address(order_data["address"])
        page.fill_in_metro(order_data["metro"])
        page.fill_in_phone(order_data["phone"])
        page.click_to_continue()
        page.fill_in_date(order_data["date"])
        page.fill_in_period(order_data["days"])
        page.click_order()
        page.click_yes()
        assert page.check_order()
