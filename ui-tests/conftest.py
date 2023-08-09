#conftest.py is for storing fixtures and pytest-plugins
# see: https://docs.pytest.org/en/7.1.x/how-to/writing_plugins.html#conftest-py-plugins
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import logging
import os


@pytest.fixture(scope='session')
def path_to_chrome():
    return ChromeDriverManager().install()

@pytest.fixture(scope='session')
def path_to_firefox():
    return GeckoDriverManager().install()


@pytest.fixture
def return_headless_firefox_driver(path_to_firefox, base_url, request):
    webdriver_service = FirefoxService(executable_path=path_to_firefox)
    webdriver_service.start()

    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')

    driver = webdriver.Remote(webdriver_service.service_url, options=options)

    request.cls.driver = driver
    driver.get(base_url)
    yield
    driver.quit()



