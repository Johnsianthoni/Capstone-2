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
    def test_Title_validate(self, startup):
        self.driver.get(data.Data().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME,value=locators.Locators().username_input_box).send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Locators().password_input_box).send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().submit_button).click()

        self.driver.find_element(by=By.XPATH, value=locators.Locators().Admin_side_panel).click()
        #  it fetches the tile of the webpage
        print(self.driver.title)
        # it fetches the URL of the webpage
        print(self.driver.current_url)
        print()
        sleep(3)

        # Navigation of validate the title of Admin 

        User_Title = self.driver.find_element(by=By.XPATH, value=locators.Locators().User_Management).click()
        if User_Title:
           User_Title.click()
           print(User_Title)
           print(type(User_Title))
           self.driver.close()

        Job_Title = self.driver.find_element(by=By.XPATH, value=locators.Locators().Job).click()
        if Job_Title:
           Job_Title.click()
           print(Job_Title)
           print(type(Job_Title))
           self.driver.close()

        Organization_Title = self.driver.find_element(by=By.XPATH, value=locators.Locators().Organization).click()
        if Organization_Title:
           Organization_Title.click()
           print(Organization_Title)
           print(type(Organization_Title))
           self.driver.close()
        

        Qualification_Title = self.driver.find_element(by=By.XPATH, value=locators.Locators().Qualification).click()
        if Qualification_Title:
           Qualification_Title.click()
           print(Qualification_Title)
           print(type(Qualification_Title))
           self.driver.close()


        Nationalities_Title = self.driver.find_element(by=By.XPATH, value=locators.Locators().Nationalities).click()
        if Nationalities_Title:
           Nationalities_Title.click()
           print(Nationalities_Title)
           print(type(Nationalities_Title))
           

        Coroperate_Title = self.driver.find_element(by=By.XPATH, value=locators.Locators().Coroperate_Branding).click()
        if Coroperate_Title:
           Coroperate_Title.click()
           print(Coroperate_Title)
           print(type(Coroperate_Title))
          

        Configuration_Title = self.driver.find_element(by=By.XPATH, value=locators.Locators().Configuration).click()
        if Configuration_Title:
           Configuration_Title.click()
           print(Configuration_Title)
           print(type(Configuration_Title))
           self.driver.close()
       
        
        assert self.driver.title == 'OrangeHRM'
        print('SUCCESS : Logged in with Username {a} and {b}'.format(a=data.Data().username,b=data.Data().password))