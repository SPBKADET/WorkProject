from time import sleep

from selenium.webdriver.common.by import By

from UI.pages import base_page
from UI.pages.base_page import BasePage
class LoginPage(BasePage):
    def login(self):
        self.send_keys(locator=(By.XPATH,"//input[@name='login']"),send_imput="")
        self.send_keys(locator=(By.XPATH,"//input[@name='password"),send_imput="")
        for i in range(10):
            self.click(locator=(By.XPATH,"//input[@name='LogonFormSubmit']"))
            if self.driver.current_url == "":
                break
            sleep(0.1)
        # assert driver.current_url == "http://172.19.165.141:8080/published?uuid=corebolg85k6o0000l5rq0pgeh34v7ao",\
        #     f'url must be equal to http://172.19.165.141:8080/published?uuid=corebolg85k6o0000l5rq0pgeh34v7ao'
        # assert driver.find_element(by=By.XPATH,value="//a[@id='Organisations']").text=='Оргструктура',\
        #     f'Organisation must be Оргструктура'
        # sleep(3)
        # driver.close()
        # driver.quit()