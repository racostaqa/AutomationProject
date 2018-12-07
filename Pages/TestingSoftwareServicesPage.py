__author__ = 'Ricardo Acosta'

from General.Locators import Locators
from selenium.webdriver.common.by import By


class TestingSoftwareServicesPage(object):

    def __init__(self, driver):
        self.driver = driver

        # search page locators
        self.services = driver.find_element(By.XPATH, Locators.ts_services)

    def get_services(self):
        return self.services
