from selector.change_currency import Currency
from allure import title


@title("Проверка смены валюты")
def test_currency(browser, url):
    currency = Currency(browser, url)
    currency.open_browser()
    currency.change_btn()
    currency.gbr()
