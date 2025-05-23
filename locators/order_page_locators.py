from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//*[text()='{}']")
    METRO_LIST = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    CONTINUE = (By.XPATH, "//button[text()='Далее']")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_SELECT = (By.CLASS_NAME, "react-datepicker__day--selected")
    PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    DAYS = (By.XPATH, "//div[text()='{}']")
    COMPLETE_ORDER = (By.XPATH, "//button[text()='Заказать'][contains(@class, 'Button_Middle__')]")
    YES = (By.XPATH, "//button[text()='Да']")
    ORDER_REGISTERED = (By.XPATH, "//div[text()='Заказ оформлен']")
