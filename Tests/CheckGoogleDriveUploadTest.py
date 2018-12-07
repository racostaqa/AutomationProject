__author__ = 'Ricardo'

from Pages.GoogleDrivePage import GoogleDrivePage
from Pages.GoogleAccountsPage import GoogleAccountsPage
from General.EnvironmentSetUp import EnvironmentSetUp
from General.Locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Data.Data import Data
from time import sleep
import unittest


class CheckGoogleDriveUploadTest(EnvironmentSetUp):

    def test_google_account_login(self):
        driver = self.driver
        self.driver.get(Data.GOOGLE_DRIVE_ADDRESS)
        self.driver.set_page_load_timeout(20)

        # calling Google home page
        google_drive_page = GoogleDrivePage(driver)
        self.assertTrue(google_drive_page.get_main_text().is_displayed())
        print("Google Drive page is displayed")

        # clicking on Go to Drive button
        google_drive_page.submit_go_to_drive()
        sleep(3)

        google_accounts_page = GoogleAccountsPage(driver)

        # verifying Testing Software result is shown
        self.assertTrue(google_accounts_page.get_access_text().is_displayed())
        print("Google Accounts Email page is displayed")

        # filling email field
        google_accounts_page.set_email(Data.GOOGLE_ACCOUNT_EMAIL)

        # clicking on Next Button
        google_accounts_page.submit_next_button()
        sleep(5)

        # waiting for element Password to be present
        password_web_element = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, Locators.google_account_password)))
        google_accounts_page.assign_password_object(password_web_element)

        # waiting for Next Button element to be present
        next_button_web_element = WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, Locators.google_next_btn)))
        google_accounts_page.assign_password_object(next_button_web_element)

        # waiting for Show Password Button element to be present
        show_password_button_web_element = WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, Locators.google_account_show_password_btn)))
        google_accounts_page.assign_show_password_button_object(show_password_button_web_element)

        # verifying password page is shown
        self.assertTrue(google_accounts_page.get_password().is_displayed())
        print("Google Accounts Password page is displayed")

        # clicking on Show Password button
        google_accounts_page.click_show_password_button()
        sleep(3)

        # clicking on password field
        google_accounts_page.click_password()
        sleep(3)

        # filling password field
        google_accounts_page.set_password(Data.GOOGLE_ACCOUNT_PASSWORD)
        sleep(3)

        # clicking on Next Button
        google_accounts_page.submit_next_button()
        sleep(5)


if __name__ == '__main__':
    unittest.main()
