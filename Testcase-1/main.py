# PAGE OBJECT MODEL (POM)
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Test_Data import data
from Test_Locators import locators
import pytest

class Test_Johnsi:
# Boot method to run Pytest using POM
    @pytest.fixture
    def startup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    def test_Rest_Password(self, startup):
        self.driver.get(data.Data().url)
        self.driver.implicitly_wait(10)

        # Click on the reset password button
        self.driver.find_element(by=By.XPATH,value=locators.Locators().Reset_Password).click()

        self.driver.find_element(by=By.NAME,value=locators.Locators().username_input_box).send_keys(data.Data().username)
        # Rest password successfully
        self.driver.find_element(by=By.XPATH, value=locators.Locators().Reset).click()

        assert self.driver.title == 'OrangeHRM'
        print('SUCCESS : Logged in with Username {a} '.format(a=data.Data().username))