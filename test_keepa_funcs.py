
from keepa_api import convert_to_currency, determine_good_deal, add_vars_to_list, df_loop, make_data_dict

dict_test_1 = {
    "title": "The Hobbit",
    "amazon_max_price": 2000,
    "amazon_min_price": 1000,
    "amazon_avg365_price": 1300,
    "amazon_current_price": 1200,
    "amazon_max_price_date": "2020-11-03",
    "amazon_min_price_date": "2019-12-20" 
}

dict_test_2 = {
    "title": "The Way of Kings",
    "amazon_max_price": 2550,
    "amazon_min_price": 825,
    "amazon_avg365_price": 1300,
    "amazon_current_price": 999,
    "amazon_max_price_date": "2022-12-03",
    "amazon_min_price_date": "2018-1-20" 
}

def test_convert_to_currency():

    result = convert_to_currency(dict_test_1)
    lst = [result["amazon_max_price"], result["amazon_min_price"], result["amazon_avg365_price"], result["amazon_current_price"]]
    assert lst == ["20.00", "10.00", "13.00", "12.00"]

    result2 = convert_to_currency(dict_test_2)
    lst2 = [result2["amazon_max_price"], result2["amazon_min_price"], result2["amazon_avg365_price"], result2["amazon_current_price"]]
    assert lst2 == ["25.50", "8.25", "13.00", "9.99"]

def test_determine_good_deal():
    assert determine_good_deal(2499, 899, 1247) == 22
    assert determine_good_deal(5000, 1000, 1000) == 0   
    assert determine_good_deal(5000, 1000, 5000) == 100
    assert determine_good_deal(2000, 1000, -1) == "No price history"

def test_add_vars_to_list():

    good_deal = determine_good_deal(dict_test_1["amazon_max_price"], dict_test_1["amazon_min_price"], dict_test_1["amazon_current_price"])
    result = add_vars_to_list(dict_test_1)
    lst = [result["title"], result["amazon_max_price"], result["amazon_min_price"], result["amazon_avg365_price"], result["amazon_current_price"], result["amazon_max_price_date"], result["amazon_min_price_date"], good_deal]
    expected = ["The Hobbit", "20.00", "10.00", "13.00", "12.00", "2020-11-03", "2019-12-20", good_deal]
    assert lst == expected

def test_df_loop():
    data_dict = {}
    column_names = ["Title", "Max", "Min", "Avg365", "Current", "Max Date", "Min Date", "Deal or No Deal"]
    
    df_loop(column_names, add_vars_to_list(dict_test_1), data_dict)
    
    deal = determine_good_deal(dict_test_1["amazon_max_price"], dict_test_1["amazon_min_price"], dict_test_1["amazon_current_price"])

    assert data_dict == {
        "Title": ["The Hobbit"],
        "Max": ["20.00"],
        "Min": ["10.00"],
        "Avg365": ["13.00"],
        "Current": ["12.00"],
        "Max Date": ["2020-11-03"],
        "Min Date": ["2019-12-20"],
        "Deal or No Deal": [deal]
    }