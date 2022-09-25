import os
import pytest
import logging
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Browser for run tests")
    parser.addoption("--drivers", action="store",
                     default=os.path.expanduser("C:/drivers/"),
                     help="Path to drivers")
    parser.addoption("--url", action="store",
                     default="http://192.168.1.59:8081/", help="default url")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--maximized", action="store_true",
                     help="Maximize browser windows")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", action="store", default="192.168.1.59")
    parser.addoption("--bv", action="store", default="105.0")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--logs", action="store_true")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test {} started at {}".format(request.node.name,
                                                    datetime.datetime.now()))

    if executor == "localhost":
        capabilities = {'goog:chromeOptions': {}}

        if browser_name == "chrome":
            service = ChromiumService(
                executable_path=drivers + "/chromedriver")
            driver = webdriver.Chrome(service=service)
        elif browser_name == "firefox":
            service = FFService(executable_path=drivers + "/geckodriver")
            driver = webdriver.Firefox(service=service)
        elif browser_name == "opera":
            driver = webdriver.Opera(executable_path=drivers + "/operadriver")
        elif browser_name == 'yandex':
            driver = webdriver.Chrome(
                executable_path=drivers + '/yandexdriver')
        elif browser_name == "edge":
            driver = webdriver.Edge(executable_path=drivers + "/msedgedriver")
        elif browser_name == "safari":
            driver = webdriver.Safari()
        else:
            raise ValueError(f"Browser {browser_name} is not supported.")
    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        capabilities = {
            "browserName": browser_name,
            "browserVersion": version,
            "name": "test_opencart",
            "selenoid:options": {
                "sessionTimeout": "60s",
                "enableVNC": vnc,
                "enableLog": logs
            }
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=capabilities,
        )

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    driver.maximize_window()
    driver.url = url

    def fin():
        driver.close()
        logger.info("===> Test {} finished at {}".format(request.node.name,
                                                         datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
