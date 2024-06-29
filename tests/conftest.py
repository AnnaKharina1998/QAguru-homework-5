import pytest
#from selenium import webdriver
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = '1920'
    browser.config.window_height = '3000'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 5
    yield
    browser.quit()
