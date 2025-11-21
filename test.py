import unittest
import main
import keepa_api
import harvest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class AmazonWishListTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_amazon_wish_list_name(self):
        driver = self.driver

        driver.get(f"{main.AMAZON_URL}")
        
        self.assertIn("Amazon", driver.title)

        self.tearDown()

    def test_get_isbn(self, link):
        isbn = "0316311294"

        driver = self.driver

        driver.get(link)

        self.assertEqual(harvest.get_ibn_number(driver), isbn)
        
    def tearDown(self):
        self.driver.close() 

if __name__ == "__main__":
    unittest.main()