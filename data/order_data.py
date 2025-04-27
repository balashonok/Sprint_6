from locators.main_page_locators import OrderLocators
from datetime import datetime, timedelta

today = datetime.now().strftime("%d.%m.%Y")
tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")
print(tomorrow)

ORDER_DATA = [
    {
        'button': OrderLocators.HEADER_ORDER,
        'name': 'Ольга',
        'surname': 'Балашова',
        'address': 'Красная площадь, 1',
        'metro': 'Охотный Ряд',
        'phone': '+79031231234',
        'date': today,
        'days': 'сутки'
    },
    {
        'button': OrderLocators.BOTTOM_ORDER,
        'name': 'Виктор',
        'surname': 'Петров',
        'address': 'Красная площадь, 1',
        'metro': 'Театральная',
        'phone': '+79031231234',
        'date': tomorrow,
        'days': 'семеро суток'
    }
]