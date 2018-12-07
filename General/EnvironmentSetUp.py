__author__ = 'Ricardo'

import unittest
import datetime
from selenium import webdriver


class EnvironmentSetUp(unittest.TestCase):

    # setUp contains the browser setup attributes
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Automation\\Drivers\\chromedriver.exe")
        print("run Started at: "+str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        print("----------------------------------------------------------")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    # tearDown method just to close all the browser instances and then quit
    def tearDown(self):
        if self.driver is not None:
            print("----------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at: " + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()