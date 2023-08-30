# Pytest with POM
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import data
from Test_Locators import locators
from time import sleep
import pytest


class Test_Johnsi:
    # Boot method to run Pytest using POM
    @pytest.fixture
    def startup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()
    
    # login testing
    def test_login(self, startup):

        self.driver.get(data.Data().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=locators.Locators().username_input_box).send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Locators().password_input_box).send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().submit_button).click()

        # Navigate to the validation of menu bar
        Admin = self.driver.find_element(by=By.XPATH, value=locators.Locators().Admin_url).click()
        # it fetches the tile of the webpage
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        Pim = self.driver.find_element(by=By.XPATH, value=locators.Locators().Pim_url).click()
        # it fetches the tile of the webpage
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        Leave = self.driver.find_element(by=By.XPATH, value=locators.Locators().Leave_url).click()
        # it fetches the tile of the webpage
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        Time = self.driver.find_element(by=By.XPATH, value=locators.Locators().Time_url).click()
        # it fetches the tile of the webpage
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        Recruitment = self.driver.find_element(by=By.XPATH, value=locators.Locators().Recruitment_url).click()
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        My_Info = self.driver.find_element(by=By.XPATH, value=locators.Locators().My_Info_url).click()
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        Performance = self.driver.find_element(by=By.XPATH, value=locators.Locators().Performance_url).click()
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        Dashboard = self.driver.find_element(by=By.XPATH, value=locators.Locators().Dashboard_url).click()
        # it fetches the tile of the webpage
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        Directory = self.driver.find_element(by=By.XPATH, value=locators.Locators().Directory_url).click()
        # it fetches the tile of the webpage
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        Maintenance = self.driver.find_element(by=By.XPATH, value=locators.Locators().Maintenance_url).click()
        # it fetches the tile of the webpage
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        self.driver.find_element(by=By.NAME, value=locators.Locators().password_input_box).send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().confirm_button).click()

        Claim = self.driver.find_element(by=By.XPATH, value=locators.Locators().Claim_url).click()
        # it fetches the tile of the webpage
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        Buzz = self.driver.find_element(by=By.XPATH, value=locators.Locators().Buzz_url).click()
        # it fetches the tile of the webpage
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        # Close the WebDriver
        logout_button = self.driver.find_element(by=By.XPATH, value=locators.Locators().logout_1)
        action = ActionChains(self.driver)
        action.click(on_element=logout_button)
        action.perform()
        self.driver.find_element(by=By.LINK_TEXT, value=data.Data().Logout_1).click()

        assert self.driver.title == 'OrangeHRM'

        print('SUCCESS : Logged in with Username {a} and {b}'.format(a=data.Data().username,b=data.Data().password))