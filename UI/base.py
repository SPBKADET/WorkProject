import pytest
from selenium.webdriver.chrome import webdriver

from UI.pages.login_page import LoginPage
from UI.fixtures import driver


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setUp(self, driver):
        self.driver = driver
        self.login_page= LoginPage(driver=driver)
