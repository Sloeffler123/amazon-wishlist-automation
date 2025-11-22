import unittest
import main
import keepa_api
import harvest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonWishListTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_amazon_wish_list_name(self):
        driver = self.driver

        driver.get(f"{main.AMAZON_URL}")
        
        self.assertIn("Amazon", driver.title)

        # self.tearDown()

    def test_get_isbn(self):
        
        url = "https://www.amazon.com/dp/0345466454/?coliid=I14E614AJ52EPK&colid=299PQKIASMWBC&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it_im"

        isbn = "0345466454"

        driver = self.driver

        wait = WebDriverWait(driver, 10)

        try:
            driver.get(url)
            driver.fullscreen_window()
            harvest.continue_checker(driver)
            driver.fullscreen_window()
        except NoSuchElementException:
            time.sleep(1)
            driver.get(url)

        list = wait.until(EC.presence_of_all_elements_located(harvest.get_ibn_number(driver)))

        self.assertEqual(list, isbn)
        
        # self.tearDown()

    def tearDown(self):
        self.driver.close() 

if __name__ == "__main__":
    unittest.main()