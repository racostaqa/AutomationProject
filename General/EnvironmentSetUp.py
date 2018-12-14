__author__ = 'Ricardo'

import unittest
import datetime
from selenium import webdriver


class EnvironmentSetUp(unittest.TestCase):

    # setUp contains the browser setup attributes
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Automation\\Drivers\\chromedriver.exe")
        print("----------------------------------------------------------\n")
        print("run Started at: "+str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    # tearDown method just to close all the browser instances and then quit
    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            print("Run Completed at: " + str(datetime.datetime.now()))
            print("Test Environment Destroyed")
            print("----------------------------------------------------------\n")
            cls.driver.close()
            cls.driver.quit()
