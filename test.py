import unittest
import harvest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AmazonWishListTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_amazon_wish_list(self):
        driver = self.driver
        driver.get()   