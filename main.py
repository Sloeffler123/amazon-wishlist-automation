import harvest
import setup
import keepa_api
import os
from dotenv import load_dotenv

load_dotenv()
AMAZON_URL = os.getenv("AMAZON_URL")

def main():
    driver = setup.make_driver()
    setup.open_browser(driver, AMAZON_URL)
    harvest.continue_checker(driver)
    harvest.get_data(driver)
    keepa_api.api_query()
    driver.close()
main()
