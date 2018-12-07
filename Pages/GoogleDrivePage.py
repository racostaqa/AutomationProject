__author__ = 'Ricardo Acosta'

from General.Locators import Locators
from selenium.webdriver.common.by import By


class GoogleDrivePage(object):

    def __init__(self, driver):
        self.driver = driver

        # search page locators
        self.go_to_drive_btn = driver.find_element(By.CSS_SELECTOR, Locators.google_go_to_drive_btn)
        self.main_text = driver.find_element(By.XPATH, Locators.google_main_text)

    def get_main_text(self):
        return self.main_text

    def submit_go_to_drive(self):
        self.go_to_drive_btn.click()


