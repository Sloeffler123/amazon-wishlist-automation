from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import setup

# API_KEY = 
















# def click_search_bar(webdriver, isbn_num):
#     wait = WebDriverWait(webdriver, 10)
#     search_bar = webdriver.find_element(By.XPATH, '//*[@id="sq"]')
#     wait.until(EC.element_to_be_clickable(search_bar)).click()
#     search_bar.clear()
#     search_bar.send_keys(isbn_num)
#     search_bar.send_keys(Keys.ENTER)
#     # main_camel_loop(get_csv_data(1), wait, webdriver, get_csv_data(None), get_csv_data(0))

# 0 = prices 1 = isbn
def get_csv_data(row):
    df = pd.read_csv("data.csv")
    if row is None:
        return df.columns
    else:
        return df.iloc[row]

# def main_camel_loop(isbn_nums, webdriver, book_name, current_price):
#     prices_dict = {}
#     for num, name, price in zip(isbn_nums, book_name, current_price):
#         setup.full_screen_window(webdriver)
#         click_search_bar(webdriver, num)
#         # get data
#         get_prices(prices_dict, name, price)

# def get_prices(price_dict, name, current_price):
#     low_price = lowest_ever(webdriver)
#     high_price = highest_ever(webdriver)
#     avg_price = average_price(webdriver)
#     price_dict[name] = {
#         "Lowest price": low_price,
#         "Average price": avg_price,
#         "Highest price": high_price,
#         "Current price": current_price
#     }
    
# def lowest_ever(webdriver):
#     lowest = webdriver.find_element(By.CSS_SELECTOR, "#summary_overlay_parent > div > div:nth-child(5) > div > table > tbody > tr.pt.amazon.on > td:nth-child(2)")
#     return lowest.text

# def highest_ever(webdriver):
#     highest = webdriver.find_element(By.CSS_SELECTOR, "#summary_overlay_parent > div > div:nth-child(5) > div > table > tbody > tr.pt.amazon.on > td:nth-child(3)")
#     return highest.text

# def average_price(webdriver):
#     average = webdriver.find_element(By.CSS_SELECTOR, "#summary_overlay_parent > div > div:nth-child(5) > div > table > tbody > tr.pt.amazon.on > td:nth-child(4)")
#     return average.text

