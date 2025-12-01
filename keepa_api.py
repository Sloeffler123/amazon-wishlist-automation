import os
import pandas as pd
import keepa
import time
import traceback
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("KEEPA_API_KEY")
api = keepa.Keepa(API_KEY)

def convert_to_currency(dict_for_values):
    price_list = [dict_for_values["amazon_max_price"], dict_for_values["amazon_min_price"], dict_for_values["amazon_avg365_price"], dict_for_values["amazon_current_price"]]
    price_vars = ["amazon_max_price", "amazon_min_price", "amazon_avg365_price", "amazon_current_price"]
    for price, price_var in zip(price_list, price_vars):
        price_string = str(price)
        if len(price_string) == 4:
           dict_for_values[price_var] = f"{price_string[:2]}.{price_string[2:]}"
        else:
            dict_for_values[price_var] = f"{price_string[:1]}.{price_string[1:]}"
    return dict_for_values

def determine_good_deal(max, min, current):
    max_int = float(max)
    min_int = float(min)
    current_int = float(current)
    if -0.1 in (max_int, min_int, current_int):
        return "No price history"
    deal = (current_int - min_int) / (max_int - min_int) * 100
    return round(deal) 

def add_vars_to_list(dict_for_values):
    dict_for_values["Deal or No Deal"] = determine_good_deal(dict_for_values["amazon_max_price"], dict_for_values["amazon_min_price"], dict_for_values["amazon_current_price"])
    return dict_for_values

def make_data_dict(dict_for_values, data_dict):
    column_names = ["Title", "Max", "Min", "Avg365", "Current", "Max Date", "Min Date", "Deal or No Deal"]
    df_loop(column_names, add_vars_to_list(dict_for_values), data_dict)
    return data_dict

def df_loop(column_names, dict_for_values, data_dict):
    for name, data  in zip(column_names, dict_for_values.values()):
        if data_dict.get(name) is not None:
            data_dict[name].append(data)
        else:
            data_dict[name] = [data]    
    return dict_for_values

def main_loop(isbn_list, data_dict):
    for i in range(len(isbn_list)):
        try:
            dictionary_for_values = {
                "title": isbn_list[i]["title"],
                "amazon_max_price" : isbn_list[i]["stats"]["max"][0][1],
                "amazon_min_price" : isbn_list[i]["stats"]["min"][0][1],
                "amazon_avg365_price" : isbn_list[i]["stats"]["avg365"][0],
                "amazon_current_price" : isbn_list[i]["stats"]["current"][0],
                "amazon_max_price_time" : isbn_list[i]["stats"]["max"][0][0],
                "amazon_min_price_time" : isbn_list[i]["stats"]["min"][0][0],
            }
            amazon_time_max_price = keepa.keepa_minutes_to_time(dictionary_for_values["amazon_max_price_time"])
            amazon_time_min_price = keepa.keepa_minutes_to_time(dictionary_for_values["amazon_min_price_time"])
            dictionary_for_values["amazon_max_price_time"] = amazon_time_max_price
            dictionary_for_values["amazon_min_price_time"] = amazon_time_min_price
            convert_to_currency(dictionary_for_values)
            make_data_dict(dictionary_for_values, data_dict)
        except TypeError:
            traceback.print_exc()
            print(f"Couldn't find {dictionary_for_values["title"]}")

def if_value_not_found(dict_for_values):
    for k, v in dict_for_values.items():
        if v < 0 or v is None:
            dict_for_values[k] = "Value not found"

def api_query():
    with open("data_file.txt", "r") as isbn_list:
        isbn_list = [line.rstrip("\n") for line in isbn_list]
    all_data_dict = {}
    asin_query = api.query(items=isbn_list, history=False, to_datetime=False, out_of_stock_as_nan=False, progress_bar=False, wait=False, offers=None, stock=False, stats=0)
    try:
        main_loop(asin_query, all_data_dict)
    except TimeoutError:
        time.sleep(10)
        main_loop(asin_query, all_data_dict)
    df = pd.DataFrame(all_data_dict)
    df.to_csv("main_csv_data.csv", index=False)