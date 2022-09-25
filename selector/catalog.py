from selenium.webdriver.common.by import By
from selector.BasePage import BasePage
from allure import step


class CatalogSelector:
    POSTFIX_URL = "/desktops"
    desktops = (By.CSS_SELECTOR, "div#content > h2")
    mac = (By.XPATH, "//div[@class='list-group']//a[1]")
    check_mac = (By.CSS_SELECTOR, "div:nth-of-type(4) > div:nth-of-type(7)")
    components = (By.XPATH, "//a[contains(text(),'Components')]")
    monitors = (By.XPATH, "//a[contains(text(),'Monitors (2)')]")
    check_monitors = (By.CSS_SELECTOR, "h2")
    tablets = (By.XPATH, "//a[contains(text(),'Tablets')]")
    check_tablets = (By.CSS_SELECTOR, "h2")
    software = (By.XPATH, "//a[contains(text(),'Software')]")
    check_software = (By.CSS_SELECTOR, "h2")
    phones = (By.XPATH, "//a[contains(text(),'Phones & PDAs')]")
    check_phones = (By.CSS_SELECTOR, "h2")


class Catalog(BasePage):

    def open(self, url):
        self.browser.get(url + CatalogSelector.POSTFIX_URL)

    @step("Открыть раздел Desktop")
    def check_desktop(self):
        desktop = self.find_element_with_wait(CatalogSelector.desktops)
        return desktop

    @step("Открыть раздел Mac")
    def check_mac(self):
        mac = self.find_element_with_wait(CatalogSelector.mac)
        return mac

    @step("Открыть раздел Components")
    def check_components(self):
        components = self.find_element_with_wait(CatalogSelector.components)
        return components

    @step("Открыть раздел Monitors")
    def check_monitors(self):
        monitors = self.find_element_with_wait(CatalogSelector.monitors)
        return monitors

    @step("Открыть раздел Tablets")
    def check_tablets(self):
        tablets = self.find_element_with_wait(CatalogSelector.tablets)
        return tablets

    @step("Открыть раздел Software")
    def check_software(self):
        software = self.find_element_with_wait(CatalogSelector.software)
        return software

    @step("Открыть раздел Phones")
    def check_phone(self):
        phone = self.find_element_with_wait(CatalogSelector.phones)
        return phone

    @step("Проверить наличие Mac")
    def mac_check(self):
        mac_check = self.find_element_with_wait(CatalogSelector.check_mac)
        return mac_check

    @step("Проверить наличие монитора")
    def monitors_check(self):
        monitors_check = self.find_element_with_wait(
            CatalogSelector.check_monitors)
        return monitors_check

    @step("Проверить наличие планшетов")
    def tablets_check(self):
        tablets_check = self.find_element_with_wait(
            CatalogSelector.check_tablets)
        return tablets_check

    @step("Проверить наличие софта")
    def software_check(self):
        software_check = self.find_element_with_wait(
            CatalogSelector.check_software)
        return software_check

    @step("Проверить наличие телефонов")
    def phones_check(self):
        phones_check = self.find_element_with_wait(
            CatalogSelector.check_phones)
        return phones_check
