from selenium.webdriver.common.by import By
from selector.BasePage import BasePage
from allure import step


class AdminPageSelector:
    POSTFIX_URL = "/admin"
    img = (By.CSS_SELECTOR, "img[title='OpenCart']")
    username = (By.CSS_SELECTOR, "#input-username")
    password = (By.CSS_SELECTOR, "#input-password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    panel = (By.CSS_SELECTOR, ".panel-title")


class AdminPage(BasePage):

    def open(self, url):
        self.browser.get(url + AdminPageSelector.POSTFIX_URL)

    @step("Проверка заголовка")
    def check_name(self):
        img = self.find_element_with_wait(AdminPageSelector.img)
        return img

    @step("Проверка поля username")
    def check_username(self):
        username = self.find_element_with_wait(AdminPageSelector.username)
        return username

    @step("Проверка поля password")
    def check_password(self):
        password = self.find_element_with_wait(AdminPageSelector.password)
        return password

    @step("Проверка кнопки login")
    def check_login(self):
        login_button = self.find_element_with_wait(
            AdminPageSelector.login_button)
        return login_button

    @step("Проверка наличии надписи")
    def check_panel(self):
        panel = self.find_element_with_wait(AdminPageSelector.panel)
        return panel

    def check_img(self):
        pass
