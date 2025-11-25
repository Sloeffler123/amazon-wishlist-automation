from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def continue_checker(webdrive):
    try:
        button = webdrive.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div/form/div/div/span/span/button")
        if button:
            button.click()
            webdrive.fullscreen_window()
            time.sleep(2)
    except NoSuchElementException:
        print("Button wasnt there")

def get_data(webdriver):
    infinite_scroll(webdriver)
    asin_list = webdriver.find_elements(By.CSS_SELECTOR, "[data-csa-c-item-id]")
    asin_set = set()
    for num in asin_list:
        num = num.get_attribute("data-csa-c-item-id")
        if "asin" in num:
            continue
        elif num in asin_set:
            continue
        else:
            asin_set.add(num)
    with open ("data_file.txt", "w") as f:
        f.write("\n".join(asin_set))

def infinite_scroll(webdriver):
    last_height = webdriver.execute_script("return document.body.scrollHeight")
    while True:
        webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = webdriver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height