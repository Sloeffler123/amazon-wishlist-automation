import harvest
import setup
import keepa_api
AMAZON_URL = "https://www.amazon.com/hz/wishlist/ls/299PQKIASMWBC/ref=nav_wishlist_lists_1"

def main():
    driver = setup.make_driver()
    setup.open_browser(driver, AMAZON_URL)
    harvest.continue_checker(driver)
    harvest.get_data(driver)
    

main()


#get the asin by using data-csa-c-item-id
#try infinite scroll to load all products
#check if there are more pages at end of list
#clean up try excepts