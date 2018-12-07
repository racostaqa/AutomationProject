__author__ = 'Ricardo Acosta'

from General.Locators import Locators
from selenium.webdriver.common.by import By


class GoogleSearchResultPage(object):

    def __init__(self, driver):
        self.driver = driver

        # search result page locators
        self.testing_software_result = driver.find_element(By.XPATH, Locators.testing_software_result)

    def get_testing_software_result(self):
        return self.testing_software_result

    def click_testing_software_result(self):
        self.testing_software_result.click()

