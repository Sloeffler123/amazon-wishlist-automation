import harvest
import setup


def main():
    driver = setup.make_driver()
    setup.open_browser(driver)
    harvest.continue_checker(driver)
    # harvest.scroll_loop(driver)
    harvest.get_data(driver)
    # title_names = harvest.get_names(driver)
    # price_books = harvest.get_prices(driver)
    # links  = harvest.get_links(driver)
    # harvest.combine_names_prices(title_names, price_books)
    # harvest.get_ibn_number(driver, links)


main()