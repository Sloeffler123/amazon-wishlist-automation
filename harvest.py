from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time
URL = "https://www.amazon.com/hz/wishlist/ls/299PQKIASMWBC/ref=nav_wishlist_lists_1"

def make_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def open_browser(webdrive):
    webdrive.get(URL)
    webdrive.fullscreen_window()
    time.sleep(2)

def clear_empty_elems(list):
    new_list = []
    for i in list: 
        if len(i.text) < 1:
            continue
        else:
            new_list.append(i)
    return new_list        

def scroll_loop(webdrive):
    scroll_to =  webdrive.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/div[8]/div/div/ul/li[11]")
    scroll_origin = ScrollOrigin.from_element(scroll_to)
    ActionChains(webdrive).scroll_from_origin(scroll_origin, 0, 700).perform()
    time.sleep(3)
    not_end = True
    while not_end:
        ActionChains(webdrive).scroll_by_amount(0, 700).perform()
        time.sleep(2)
        if webdrive.find_element(By.TAG_NAME, "h5").text == "End of list":
            not_end = False

def continue_checker(webdrive):
    try:
        button = webdrive.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/form/div/div/span/span/button")
        if button:
            button.click()
            webdrive.fullscreen_window()
            time.sleep(2)
    except NoSuchElementException:
        print("Button wasnt there")


def get_names_prices(webdrive):
    title_names = webdrive.find_elements(By.TAG_NAME, "h2")
    price_for_books = webdrive.find_elements(By.CLASS_NAME, "a-price")
    new_title_names = clear_empty_elems(title_names)
    return new_title_names, price_for_books

def combine_names_prices(title_names, price_books):
    book_price_dict = {}
    for name, price in zip(title_names, price_books):
        if len(name.text) < 1:
            continue
        
        book_price_dict[name.text] = price.text
    print(book_price_dict)
