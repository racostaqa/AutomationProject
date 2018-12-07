__author__ = 'Ricardo Acosta'

from General.Locators import Locators
from selenium.webdriver.common.by import By


class GoogleAccountsPage(object):

    def __init__(self, driver):
        self.driver = driver

        # search page locators
        self.email = driver.find_element(By.CSS_SELECTOR, Locators.google_account_email)
        # self.password = driver.find_element(By.XPATH, Locators.google_account_password)
        self.next_button = driver.find_element(By.XPATH, Locators.google_next_btn)
        self.access_text = driver.find_element(By.XPATH, Locators.google_access_text)
        # self.show_password_btn = driver.find_element(By.XPATH, Locators.google_account_show_password_btn)

    def get_access_text(self):
        return self.access_text

    def set_email(self, email):
        self.email.send_keys(email)

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password.send_keys(password)

    def click_password(self):
        self.password.click()

    def assign_password_object(self, web_element):
        self.password = web_element

    def get_next_button(self):
        return self.next_button

    def submit_next_button(self):
        self.next_button.click()

    def assign_next_button_object(self, web_element):
        self.next_button = web_element

    def get_show_password_button(self):
        return self.show_password_btn

    def click_show_password_button(self):
        self.show_password_btn.click()

    def assign_show_password_button_object(self, web_element):
        self.show_password_btn = web_element
