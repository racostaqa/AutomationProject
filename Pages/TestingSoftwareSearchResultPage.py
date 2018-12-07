__author__ = 'Ricardo Acosta'

from General.Locators import Locators
from selenium.webdriver.common.by import By


class TestingSoftwareSearchResultPage(object):

    def __init__(self, driver):
        self.driver = driver

        # search page locators
        self.search_result = driver.find_element(By.XPATH, Locators.ts_search_result)

    def get_search_result(self):
        return self.search_result


