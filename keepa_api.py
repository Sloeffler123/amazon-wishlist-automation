import os
import pandas as pd
import keepa
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("KEEPA_API_KEY")

api = keepa.Keepa(API_KEY)

# seperate from ISBN-10 from ISBN-13
# 1 gets isbn 0 gets prices None gets names
def get_csv_data(row):
    df = pd.read_csv("data.csv")
    if row is None:
        return df.columns
    else:
        return df.iloc[row]


def seperate_ISBN10_ISBN13():
    nums = get_csv_data(1)
    isbn_13 = []
    isbn_10 = []
    for num in nums:
        if "-" in num:
            isbn_13.append(num)
        else:
            isbn_10.append(num)        
    return isbn_10, isbn_13

def convert_to_currency(max, min, avg, current):
    
    lst = [max, min, avg, current]
    new_lst = []
    for i in lst:
        j = str(i)
        if len(j) == 4:
           num = f"${j[0:2]}.{j[2:4]}"
        else:
            num = f"${j[0:1]}.{j[1:3]}"
        new_lst.append(num)        
    
    return new_lst    

def add_vars_to_list(data_list, name, max_date, min_date):
    data_list.append(max_date)
    data_list.append(min_date)
    main_list = [name] + data_list
    return main_list

def make_data_dict(max, min, avg, current, max_date, min_date, count):
    column_names = ["Title", "Max", "Min", "Avg365", "Current", "Max Date", "Min Date"]
    names = get_csv_data(None)
    data_dict = df_loop(column_names, add_vars_to_list(convert_to_currency(max, min, avg, current), names[count], max_date, min_date))

def df_loop(column_names, main_list):
    data_dict = {}
    for name, data  in zip(column_names, main_list):
        if data_dict.get(name) is not None:
            data_dict[name].append(data)
        else:
            data_dict[name] = [data]    

def main_loop(isbn_list):
    # need to make dict here
    for i in range(len(isbn_list)):

        amazon_current_price = isbn_list[i]["stats"]["current"][0]
        amazon_max_price = isbn_list[i]["stats"]["max"][0][1]
        amazon_max_price_time = isbn_list[i]["stats"]["max"][0][0]
        amazon_time_max_price = keepa.keepa_minutes_to_time(amazon_max_price_time)
        amazon_min_price = isbn_list[i]["stats"]["min"][0][1]
        amazon_min_price_time = isbn_list[i]["stats"]["min"][0][0]
        amazon_time_min_price = keepa.keepa_minutes_to_time(amazon_min_price_time)
        amazon_avg365_price = isbn_list[i]["stats"]["avg365"][0]

        data = make_data_dict(amazon_max_price, amazon_min_price, amazon_avg365_price, amazon_current_price, amazon_time_max_price, amazon_time_min_price, i)
    print(data)    

def api_query():
    
    isbn_10, isbn_13 = seperate_ISBN10_ISBN13()
    test = [isbn_10[0], isbn_10[1], isbn_10[2], isbn_10[3], isbn_10[4]]
    isbn_10_products = api.query(items=test, history=False, to_datetime=False, out_of_stock_as_nan=False, progress_bar=False, buybox=False, wait=False, offers=None, stock=False, stats=0)
    # get the current price from api
    main_loop(isbn_10_products)
    

api_query()
