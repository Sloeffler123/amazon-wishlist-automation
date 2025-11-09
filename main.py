import harvest
import setup
import camel
AMAZON_URL = "https://www.amazon.com/hz/wishlist/ls/299PQKIASMWBC/ref=nav_wishlist_lists_1"

CAMEL_URL = "https://camelcamelcamel.com/"

def main():
    driver = setup.make_driver()
    setup.open_browser(driver, AMAZON_URL)
    # harvest.continue_checker(driver)
    # harvest.get_data(driver)
    driver.switch_to.new_window("tab")
    setup.open_browser(driver, CAMEL_URL)
    camel.read_isbn()











    # title_names = harvest.get_names(driver)
    # price_books = harvest.get_prices(driver)
    # links  = harvest.get_links(driver)
    # harvest.combine_names_prices(title_names, price_books)
    # harvest.get_ibn_number(driver, links)


main()