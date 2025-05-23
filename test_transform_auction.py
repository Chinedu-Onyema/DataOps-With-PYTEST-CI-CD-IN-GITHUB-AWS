import pandas as pd
import numpy as np
import pytest

# importing all the defined functions from our transform_auction.py
from transform_auction import (
    read_url_table,
    clean_url_column,
    clean_condition_column,
    clean_vin_column,
    clean_transmission_column,
    clean_mileage_column,
    clean_fuel_type_column,
    clean_the_overall_table,
    clean_the_price_column,
)


# I had to mock the csv files and use the pandas dataframe to test
# each data cleaning fuction without reading and writing on the original "Unclean_Raw_Scrapped_bidding_data.csv" csv file.
@pytest.fixture
def simulated_data_structure():
    data_structure = {
        "URL": ["https://site.com/item?refNo=123"],
        "Reference Number": ["REF123"],
        "Price": ["₦1,000,000"],
        "Car Title": ["Toyota Corolla"],
        "Condition": ["Nigeria"],
        "VIN": ["Used"],
        "Transmission": ["AUTOMATIC"],
        "Mileage": ["0.00KM"],
        "Fuel Type": ["PETROL"],
        "Unnamed: 0": [0],
    }
    return pd.DataFrame(data_structure)


def test_clean_url_column(simulated_data_structure):
    df = clean_url_column(simulated_data_structure.copy())
    assert df["URL"][0] == "123"


def test_clean_condition_column(simulated_data_structure):
    df = clean_condition_column(simulated_data_structure.copy())
    assert df["Condition"][0] == "Nigeria"


def test_clean_vin_column(simulated_data_structure):
    df = clean_vin_column(simulated_data_structure.copy())
    assert df["VIN"][0] == "Used"


def test_clean_transmission_column(simulated_data_structure):
    df = clean_transmission_column(simulated_data_structure.copy())
    assert df["Transmission"][0] == "AUTOMATIC"


def test_clean_mileage_column(simulated_data_structure):
    df = clean_mileage_column(simulated_data_structure.copy())
    assert df["Mileage"][0] == "0.00KM"


def test_clean_fuel_type_column(simulated_data_structure):
    df = clean_fuel_type_column(simulated_data_structure.copy())
    assert df["Fuel Type"][0] == "PETROL"


def test_clean_the_overall_table(simulated_data_structure):
    df = simulated_data_structure.copy()
    df = clean_url_column(df)
    df = clean_condition_column(df)
    df = clean_vin_column(df)
    df = clean_transmission_column(df)
    df = clean_mileage_column(df)
    df = clean_fuel_type_column(df)
    df = clean_the_overall_table(df)

    expected_columns = [
        "Bidding_Item",
        "Reference_Number",
        "Bid_Winning_Price",
        "Bidding_Item_Title",
        "Bid_Item_Identification_Number",
        "Condition",
        "Transmission_Type",
        "Fuel_Type",
    ]
    assert all(col in df.columns for col in expected_columns)
    assert df.index[0] == 0


def test_clean_the_price_column(simulated_data_structure):
    df = simulated_data_structure.copy()
    df = clean_the_overall_table(df)
    df = clean_the_price_column(df)

    assert isinstance(df["Bid_Winning_Price"][0], float)
    assert df["Bid_Winning_Price"][0] == 1000000.0
