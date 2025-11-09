from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time



def make_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def tear_down(webdriver):
    webdriver.quit()

def open_browser(webdrive, url):
    webdrive.get(url)
    webdrive.fullscreen_window()
    time.sleep(2)