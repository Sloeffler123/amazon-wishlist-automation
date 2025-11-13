import os
import pandas as pd
import keepa
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("KEEPA_API_KEY")

api = keepa.Keepa(API_KEY)

# seperate from ISBN-10 from ISBN-13
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
           num = f"{j[0:2]}.{j[2:4]}"
        else:
            num = f"{j[0:1]}.{j[1:3]}"
        new_lst.append(num)        
        
    print(new_lst)    

def api_query():
    
    isbn_10, isbn_13 = seperate_ISBN10_ISBN13()

    isbn_10_products = api.query(items=isbn_10[0], history=False, to_datetime=False, out_of_stock_as_nan=False, progress_bar=False, buybox=False, wait=False, offers=None, stock=False, stats=0)

    amazon_current_price = isbn_10_products[0]["stats"]["current"][0]

    amazon_max_price = isbn_10_products[0]["stats"]["max"][0][1]
    amazon_max_price_time = isbn_10_products[0]["stats"]["max"][0][0]
    
    amazon_min_price = isbn_10_products[0]["stats"]["min"][0][1]
    amazon_min_price_time = isbn_10_products[0]["stats"]["min"][0][0]

    amazon_avg365_price = isbn_10_products[0]["stats"]["avg365"][0]

    convert_to_currency(amazon_max_price, amazon_min_price, amazon_avg365_price, amazon_current_price)

api_query()
