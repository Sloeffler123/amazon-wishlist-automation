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


def clear_empty_elems(list):
    new_list = []
    for i in list: 
        if len(i.text) < 1:
            continue
        else:
            new_list.append(i)
    return new_list        

def continue_checker(webdrive):
    try:
        button = webdrive.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/form/div/div/span/span/button")
        if button:
            button.click()
            webdrive.fullscreen_window()
            time.sleep(2)
    except NoSuchElementException:
        print("Button wasnt there")

def get_names(webdrive):
    title_names = webdrive.find_elements(By.TAG_NAME, "h2")
    new_title_names = clear_empty_elems(title_names)
    return new_title_names

def get_links(webdrive):
    links = webdrive.find_elements(By.CSS_SELECTOR, "h2 a")
    return links

def get_prices(webdrive):
    price_for_books = webdrive.find_elements(By.CLASS_NAME, "a-price")
    return price_for_books

def get_ibn_number(webdriver):
    ibn_num = webdriver.find_element(By.CSS_SELECTOR, "#detailBulletsWrapper_feature_div")
    ibn_list = ibn_num.text.split()
    return get_ibn_loop(ibn_list)

def get_ibn_loop(ibn_list):
    for i in range(len(ibn_list)):
        if ibn_list[i] == "ISBN-10" or ibn_list[i] == "ISBN-13":
            return ibn_list[i+2]
        
def combine_names_prices(title_names, price_books):
    book_price_dict = {}
    for name, price in zip(title_names, price_books):
        if len(name.text) < 1:
            continue
        
        book_price_dict[name.text] = price.text
    print(book_price_dict)


def get_data(webdriver):
    wait = WebDriverWait(webdriver, 10)
    i = 0
    names_list_holder = []
    book_price_data = {}
    while True:
        time.sleep(6)
        get_names_func = get_names(webdriver)
        get_links_func = get_links(webdriver)
        print(f"{i} - {len(get_links_func)}")
        if get_names_func[i] not in names_list_holder:
            elem = get_names_func[i]
            name = elem.text
            get_data_helper(elem, i, book_price_data, names_list_holder, webdriver)
            time.sleep(0.5)
            ActionChains(webdriver).scroll_to_element(elem).perform()
            ActionChains(webdriver).scroll_by_amount(0, 300).perform()
            try:
                time.sleep(0.5)
                wait.until(EC.element_to_be_clickable(get_links_func[i])).click()
            except IndexError:
                print("index error")
                ActionChains(webdriver).scroll_(elem).perform()
                wait.until(EC.element_to_be_clickable(get_links_func[i])).click()
            webdriver.fullscreen_window()
            ibn_num = get_ibn_number(webdriver)
            book_price_data[name].append(ibn_num)
            setup.go_back_open_browser(webdriver)
            i += 1
            print(f"{name} - {book_price_data[name]}")
            if i == len(get_links_func):
                break
    print(book_price_data)
    print(len(book_price_data))        
    df = pd.DataFrame(book_price_data)
    df.to_csv("data.csv", index=False)

def func_scroll_from_origin(webdriver, first_elem, link):
    time.sleep(1)
    scroll_origin = ScrollOrigin.from_element(first_elem)
    while True:
        time.sleep(1)
        if not link.click():
            ActionChains(webdriver).scroll_from_origin(scroll_origin, 0, 300).perform()
        else:
            break    

def get_data_helper(element, counter, book_price_dict, holder_list, driver):
    price = get_prices(driver)[counter].text
    name = element.text
    book_price_dict[name] = [price]
    holder_list.append(name)
