from selenium.webdriver.common.by import By
from selector.BasePage import BasePage
from allure import step


class NewUserSelector:
    my_account = (By.CSS_SELECTOR, ".caret")
    link_register = (By.CSS_SELECTOR, ".dropdown-menu>li:nth-child(1)>a")
    firstname = (By.CSS_SELECTOR, "#input-firstname")
    lastname = (By.CSS_SELECTOR, "#input-lastname")
    email = (By.CSS_SELECTOR, "#input-email")
    telephone = (By.CSS_SELECTOR, "#input-telephone")
    password = (By.CSS_SELECTOR, "#input-password")
    confirm = (By.CSS_SELECTOR, "#input-confirm")
    privacy = (By.CSS_SELECTOR, ".pull-right>input:nth-child(2)")
    continue_btn = (By.CSS_SELECTOR, ".btn-primary")


class NewUser(BasePage):
    @step("Нажать кнопку добавления аккаунта")
    def my_account(self):
        my_account = self.find_element_with_wait(
            NewUserSelector.my_account).click()
        return my_account

    @step("Нажать кнопку регистрации")
    def link_register(self):
        link_register = self.find_element_with_wait(
            NewUserSelector.link_register).click()
        return link_register

    @step("Ввести имя")
    def input_first_name(self):
        first_name = self.find_element_with_wait(
            NewUserSelector.firstname).send_keys("John")
        return first_name

    @step("Ввести фамилию")
    def input_last_name(self):
        last_name = self.find_element_with_wait(
            NewUserSelector.lastname).send_keys("Doe")
        return last_name

    @step("Ввести почту")
    def input_email(self):
        email = self.find_element_with_wait(NewUserSelector.email).send_keys(
            "testing@gmail.com")
        return email

    @step("Ввести телефон")
    def input_telephone(self):
        telephone = self.find_element_with_wait(
            NewUserSelector.telephone).send_keys("+79998887766")
        return telephone

    @step("Ввести пароль")
    def input_password(self):
        password = self.find_element_with_wait(
            NewUserSelector.password).send_keys("123456789")
        return password

    @step("Подтвердить пароль")
    def input_confirm(self):
        confirm = self.find_element_with_wait(
            NewUserSelector.confirm).send_keys("123456789")
        return confirm

    @step("Нажать на чек-бокс принятия условий")
    def privacy(self):
        privacy = self.find_element_with_wait(NewUserSelector.privacy).click()
        return privacy

    @step("Нажать кнопку Continue")
    def confirm_btn(self):
        confirm_btn = self.find_element_with_wait(
            NewUserSelector.continue_btn).click()
        return confirm_btn
