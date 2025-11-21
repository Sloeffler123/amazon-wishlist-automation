
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import setup

def continue_checker(webdrive):
    try:
        button = webdrive.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/form/div/div/span/span/button")
        if button:
            button.click()
            webdrive.fullscreen_window()
            time.sleep(2)
    except NoSuchElementException:
        print("Button wasnt there")

def get_links(webdrive):
    links = webdrive.find_elements(By.CSS_SELECTOR, "h2 a")
    return links

def get_ibn_number(webdriver):
    ibn_num = webdriver.find_element(By.CSS_SELECTOR, "#detailBulletsWrapper_feature_div")
    ibn_list = ibn_num.text.split()
    return get_ibn_loop(ibn_list)

def get_ibn_loop(ibn_list):
    for i in range(len(ibn_list)):
        if ibn_list[i] == "ISBN-10" or ibn_list[i] == "ISBN-13":
            return ibn_list[i+2]
        
def get_data(webdriver):
    wait = WebDriverWait(webdriver, 10)
    i = 0
    links_list_holder = []
    # book_price_data = {}
    isbn_list = []
    while True:
        time.sleep(7)
        # get_names_func = get_names(webdriver)
        get_links_func = get_links(webdriver)
        print(f"{i} - {len(get_links_func)}")
        if get_links_func[i] not in links_list_holder:
            elem = get_links_func[i]
            # get_data_helper(elem, i, book_price_data, names_list_holder, webdriver)
            click_elem(elem, webdriver, wait)
            isbn_num = get_ibn_number(webdriver)
            isbn_list.append(isbn_num)
            setup.go_back_open_browser(webdriver)
            i += 1
            print(f"{isbn_num}")
            if i == len(get_links_func):
                break
    print(isbn_list)
    print(len(isbn_list))  
    with open ("data_file.txt", "w") as f:
        f.write("\n".join(isbn_list))

def click_elem(elem, webdriver, wait):
    time.sleep(0.5)
    ActionChains(webdriver).scroll_to_element(elem).perform()
    ActionChains(webdriver).scroll_by_amount(0, 300).perform()
    try:
        time.sleep(0.5)
        wait.until(EC.element_to_be_clickable(elem)).click()
    except IndexError:
        print("index error")
        ActionChains(webdriver).scroll_(elem).perform()
        wait.until(EC.element_to_be_clickable(elem)).click()
    webdriver.fullscreen_window()
