import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Клик на кнопку "Заказать"')
    def click_to_order(self, button):
        self.click_to_element_with_wait(button)

    @allure.step('Заполнение имени')
    def fill_in_name(self, name):
        self.add_text_to_element(OrderPageLocators.NAME, name)

    @allure.step('Заполнение фамилии')
    def fill_in_surname(self, surname):
        self.add_text_to_element(OrderPageLocators.SURNAME, surname)

    @allure.step('Заполнение адреса')
    def fill_in_address(self, address):
        self.add_text_to_element(OrderPageLocators.ADDRESS, address)

    @allure.step('Заполнение станции метро')
    def fill_in_metro(self, metro):
        self.click_to_element_with_wait(OrderPageLocators.METRO_LIST)
        locator_formatted = self.format_locators(OrderPageLocators.METRO, metro)
        self.click_to_element_with_wait(locator_formatted)

    @allure.step('Заполнение телефона')
    def fill_in_phone(self, phone):
        self.add_text_to_element(OrderPageLocators.PHONE, phone)

    @allure.step('Нажатие кнопки "Далее"')
    def click_to_continue(self):
        self.click_to_element(OrderPageLocators.CONTINUE)

    @allure.step('Заполнение даты')
    def fill_in_date(self, date):
        self.add_text_to_element(OrderPageLocators.DATE, date)
        self.click_to_element_with_wait(OrderPageLocators.DATE_SELECT)

    @allure.step('Заполнение периода')
    def fill_in_period(self, days):
        self.click_to_element_with_wait(OrderPageLocators.PERIOD)
        locator_formatted = self.format_locators(OrderPageLocators.DAYS, days)
        self.click_to_element_with_wait(locator_formatted)

    @allure.step('Нажать "Далее"')
    def click_order(self):
        self.click_to_element_with_wait(OrderPageLocators.COMPLETE_ORDER)

    @allure.step('Нажать "Да"')
    def click_yes(self):
        self.click_to_element_with_wait(OrderPageLocators.YES)

    @allure.step('Проверка отображения заголовка "Заказ оформлен"')
    def check_order(self):
        return self.is_displayed(OrderPageLocators.ORDER_REGISTERED)
