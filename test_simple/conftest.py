

import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_management(driver_options=webdriver.ChromeOptions()):
    browser.config.base_url = "https://t1.ru/"
    browser.config.window_width = 3840
    browser.config.window_height = 2160
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    yield
    browser.quit()
