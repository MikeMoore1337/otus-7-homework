from selector.main_page import MainPage
from allure import title


@title("Проверка наличия логотипа")
def test_check_name(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_name()


@title("Проверка наличия кнопки корзины")
def test_check_cart(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_cart()


@title("Проверка наличия macbook")
def test_check_macbook(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_macbook()


@title("Проверка наличия строки поиска")
def test_check_search(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_search()


@title("Проверка наличия продукта")
def test_check_product(browser, url):
    main = MainPage(browser, url)
    main.open_browser()
    main.check_product()
