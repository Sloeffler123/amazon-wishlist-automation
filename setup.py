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

def tear_down(webdriver):
    webdriver.quit()

def open_browser(webdrive):
    webdrive.get(URL)
    webdrive.fullscreen_window()
    time.sleep(2)