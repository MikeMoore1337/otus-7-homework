from selector.new_user import NewUser
from allure import title


@title("Проверка создания нового пользователя")
def test_new_user(browser, url):
    newuser = NewUser(browser, url)
    newuser.open_browser()
    newuser.my_account()
    newuser.link_register()
    newuser.input_first_name()
    newuser.input_last_name()
    newuser.input_email()
    newuser.input_telephone()
    newuser.input_password()
    newuser.input_confirm()
    newuser.privacy()
    newuser.confirm_btn()
