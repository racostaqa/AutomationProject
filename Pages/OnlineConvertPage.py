__author__ = 'Ricardo Acosta'

from General.Locators import Locators
from selenium.webdriver.common.by import By


class OnlineConvertPage(object):

    def __init__(self, driver):
        self.driver = driver

        # search page locators
        self.file_input_btn = driver.find_element(By.CSS_SELECTOR, Locators.online_convert_input_file)
        self.logo = driver.find_element(By.CSS_SELECTOR, Locators.online_convert_logo)
        self.convert_btn = driver.find_element(By.CSS_SELECTOR, Locators.online_convert_submit_btn)
        # self.success_message = driver.find_element(By.XPATH, Locators.online_convert_success_txt)

    def get_file_input_btn(self):
        return self.file_input_btn

    def send_keys_file_input_btn(self, file_location):
        self.file_input_btn.send_keys(file_location)

    def get_logo(self):
        return self.logo

    def submit_convert_btn(self):
        self.convert_btn.click()

    def get_success_message(self):
        return self.success_message

    def set_success_message(self, web_element):
        self.success_message = web_element
