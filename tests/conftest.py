import pytest
from selene import browser
from selene.support.shared import config


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    config.window_width = 1920
    config.window_height = 1080

    yield
    browser.quit()
