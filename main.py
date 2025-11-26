import harvest
import setup
import keepa_api

AMAZON_URL = "https://www.amazon.com/hz/wishlist/ls/299PQKIASMWBC/ref=nav_wishlist_lists_1"

def main():
    driver = setup.make_driver()
    setup.open_browser(driver, AMAZON_URL)
    harvest.continue_checker(driver)
    harvest.get_data(driver)
    keepa_api.api_query()
    driver.close()
main()
