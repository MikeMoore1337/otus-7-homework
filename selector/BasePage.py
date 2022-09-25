import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException, \
    ElementNotInteractableException


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_browser(self):
        self.browser.logger.info("Opening url: {}".format(self.url))
        self.browser.get(self.url)

    def find_element_with_wait(self, locator, timeout=10):
        self.browser.logger.info(
            "Finding element with wait: {}".format(locator))
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            raise allure.attach(self.browser.get_screenshot_as_png(),
                                name="screenshot",
                                attachment_type=AttachmentType.PNG)
        return element

    def find_element_with_wait_clickable(self, locator, timeout=10):
        self.browser.logger.info(
            "Finding element with wait clickable: {}".format(locator))
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(
                "Не найден элемент с селектором: {}".format(locator))
        except ElementNotInteractableException:
            raise allure.attach(self.browser.get_screenshot_as_png(),
                                name="screenshot",
                                attachment_type=AttachmentType.PNG)
        return element
