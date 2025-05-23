from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_LOCATORS = (By.ID, 'accordion__heading-{}')
    ANSWER_LOCATORS = (By.ID, 'accordion__panel-{}')
    QUESTION_LOCATOR_TO_SCROLL = (By.ID, 'accordion__heading-7')

class OrderLocators:
    HEADER_ORDER = (By.XPATH, "//button[text()='Заказать']")
    BOTTOM_ORDER = (
    By.XPATH, "//button[text()='Заказать']/parent::div[contains(@class, 'Home_FinishButton__1')]")  # Кнопка Заказать внизу страницы

class AcceptCookieLocators:
    ACCEPT_COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")