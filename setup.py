from selenium import webdriver
import time

def make_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-features=PushMessaging,MessagingService")
    chrome_options.add_argument("--disable-background-networking")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--user-data-dir=C:/Temp/selenium-clean")
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def tear_down(webdriver):
    webdriver.quit()

def open_browser(webdrive, url):
    webdrive.get(url)
    time.sleep(1)
    webdrive.fullscreen_window()
    time.sleep(2)

def go_back_open_browser(webdriver):
    time.sleep(0.5)
    webdriver.back()
    time.sleep(0.5)
    webdriver.fullscreen_window()

def full_screen_window(webdriver):
    time.sleep(0.5)
    webdriver.fullscreen_window()
    