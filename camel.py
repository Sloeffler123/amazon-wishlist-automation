from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import setup

def click_search_bar(webdriver):
    wait = WebDriverWait(webdriver, 10)
    search_bar = webdriver.find_element(By.XPATH, '//*[@id="sq"]')
    wait.until(EC.element_to_be_clickable(search_bar)).click()
    main_camel_loop(get_csv_data(1), wait, webdriver)

# 0 = prices 1 = isbn
def get_csv_data(row):
    df = pd.read_csv("data.csv")
    if row is None:
        return df.columns
    else:
        return df.iloc[row]

def main_camel_loop(isbn_nums, wait, webdriver):
    prices_dict = {}
    for num in isbn_nums:
        wait.until(EC.element_to_be_clickable(num)).click()
        setup.full_screen_window(webdriver)
        # get data
        get_prices(prices_dict)
        setup.go_back_open_browser(webdriver)

def get_prices(price_dict):
    low_price = lowest_ever(webdriver)
    high_price = highest_ever(webdriver)
    avg_price = average_price(webdriver)
    
def lowest_ever(webdriver):
    lowest = webdriver.find_element(By.CSS_SELECTOR, "#summary_overlay_parent > div > div:nth-child(5) > div > table > tbody > tr.pt.amazon.on > td:nth-child(2)")
    return lowest.text

def highest_ever(webdriver):
    highest = webdriver.find_element(By.CSS_SELECTOR, "#summary_overlay_parent > div > div:nth-child(5) > div > table > tbody > tr.pt.amazon.on > td:nth-child(3)")
    return highest.text

def average_price(webdriver):
    average = webdriver.find_element(By.CSS_SELECTOR, "#summary_overlay_parent > div > div:nth-child(5) > div > table > tbody > tr.pt.amazon.on > td:nth-child(4)")
    return average.text
