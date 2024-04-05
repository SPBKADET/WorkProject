import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from UI.pages.login_page import LoginPage


@pytest.fixture()
def driver(request):
    url="http://172.19.165.141:8080/"
    options = Options()
    options.add_argument('--window-size=1280x1696')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)

