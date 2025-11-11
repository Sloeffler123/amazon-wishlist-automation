import os
import pandas as pd
import keepa
import requests
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

def api_query():
    
    isbn_10, isbn_13 = seperate_ISBN10_ISBN13()
    test = isbn_10[0]
    print(test)
    isbn_10_products = api.query(items=test, history=False, to_datetime=False, out_of_stock_as_nan=False, progress_bar=False, buybox=False, wait=False, offers=None, stock=False, stats=0)
    
    amazon_max_price = isbn_10_products[0]["stats"]["max"][0][1]
    amazon_max_price_time = isbn_10_products[0]["stats"]["max"][0][0]
    amazon_max_price_time = (amazon_max_price_time / 60) / 24
    print(amazon_max_price_time)
    amazon_min_price = isbn_10_products[0]["stats"]["min"][0][1]
    amazon_min_price_time = isbn_10_products[0]["stats"]["min"][0][0]

    amazon_avg365_price = isbn_10_products[0]["stats"]["avg365"][0]

api_query()
