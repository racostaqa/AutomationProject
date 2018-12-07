__author__ = 'Ricardo Acosta'

from General.Locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestingSoftwareHomePage(object):

    def __init__(self, driver):
        self.driver = driver

        # search page locators
        self.search_btn = driver.find_element(By.XPATH, Locators.ts_search_btn)
        self.search_tbx = driver.find_element(By.XPATH, Locators.ts_search_tbx)
        self.home_logo = driver.find_element(By.XPATH, Locators.ts_home_logo)
        self.what_is_it_dropdown = driver.find_element(By.XPATH, Locators.ts_what_is_ts_dropdown)
        self.services_dropdown = driver.find_element(By.XPATH, Locators.ts_services_dropdown)

    def get_search_tbx(self):
        return self.search_tbx

    def set_search_tbx(self, search_string):
        self.search_tbx.clear()
        self.search_tbx.send_keys(search_string)

    def set_enter_search_tbx(self):
        self.search_tbx.send_keys(Keys.ENTER)

    def get_search_btn(self):
        return self.search_btn

    def click_search(self):
        self.search_btn.click()

    def get_home_logo(self):
        return self.home_logo

    def get_what_is_it_dropdown(self):
        return self.what_is_it_dropdown

    def click_what_is_it_dropdown(self):
        self.what_is_it_dropdown.click()

    def get_services_dropdown(self):
        return self.services_dropdown

    def click_services_dropdown(self):
        self.services_dropdown.click()
