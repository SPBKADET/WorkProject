from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self, driver):
        self.driver =driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)
    def find_element(self, locator, timeout=None):
        return self.wait(timeout).until(ec.element_to_be_clickable(locator))
    def click(self, locator, timeout=None):
        element=self.find_element(locator, timeout)
        element.click()
    def send_keys(self,locator,send_imput):
        element=self.find_element(locator=locator)
        element.clear()
        element.send_keys(send_imput)
