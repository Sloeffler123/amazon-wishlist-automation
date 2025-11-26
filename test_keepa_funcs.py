
from keepa_api import convert_to_currency, determine_good_deal, add_vars_to_list, df_loop

def test_convert_to_currency():
    result = convert_to_currency(1000, 500, 750, 900)
    assert result == ["10.00", "5.00", "7.50", "9.00"]

    result2 = convert_to_currency(5000, 3000, 3500, 3850)
    assert result2 == ["50.00", "30.00", "35.00", "38.50"]

def test_determine_good_deal():
    assert determine_good_deal(2499, 899, 1247) == 22
    assert determine_good_deal(5000, 1000, 1000) == 0   
    assert determine_good_deal(5000, 1000, 5000) == 100

def test_add_vars_to_list():
    data_list = convert_to_currency(2000, 1000, 1300, 1500)
    good_deal = determine_good_deal(2000, 1000, 1500)
    result = add_vars_to_list(data_list, "Lord of the rings", "2023-03-20", "2019-11-28")
    expected = ["Lord of the rings", "20.00", "10.00", "13.00", "15.00", "2023-03-20", "2019-11-28", good_deal]
    assert result == expected

def test_df_loop():
    data_dict = {}
    column_names = ["Title", "Max", "Min", "Avg365", "Current", "Max Date", "Min Date", "Deal or No Deal"]
    product_values = ["The Hobbit", "20.00", "8.00", "12.00", "11.00", "2024-08-22", "2018-02-01", determine_good_deal(2000, 800, 1100)]
    df_loop(column_names, product_values, data_dict)

    assert data_dict == {
        "Title": ["The Hobbit"],
        "Max": ["20.00"],
        "Min": ["8.00"],
        "Avg365": ["12.00"],
        "Current": ["11.00"],
        "Max Date": ["2024-08-22"],
        "Min Date": ["2018-02-01"],
        "Deal or No Deal": [25]
    }