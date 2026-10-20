#starts and closes the browser for each test
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver          # test runs here
    driver.quit()         # teardown, always runs