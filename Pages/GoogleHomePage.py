__author__ = 'Ricardo Acosta'

from General.Locators import Locators
from selenium.webdriver.common.by import By


class GoogleHomePage(object):

    def __init__(self, driver):
        self.driver = driver

        # search page locators
        self.search_tbx = driver.find_element(By.XPATH, Locators.google_search_tbx)
        self.search_btn = driver.find_element(By.XPATH, Locators.google_search_btn)

    def get_search_tbx(self):
        return self.search_tbx

    def set_search_tbx(self, search_string):
        self.search_tbx.clear()
        self.search_tbx.send_keys(search_string)

    def get_search_btn(self):
        return self.search_btn

    def submit_search(self):
        self.search_btn.click()


