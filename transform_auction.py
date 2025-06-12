# Bringing everything together
import pandas as pd


# import the scraped table from a csv file
def read_url_table(auction_results):
    auction_results = pd.read_csv(
        "C:\\Users\\HP\\Desktop\\Phyton for everybody with Dr Chuck\\Scrapped_Data\\Unclean_Raw_Scrapped_bidding_data.csv"
    )
    return auction_results


# split the URL column using a delimiter to get the bidding item
def clean_url_column(auction_results):
    auction_results["URL"] = auction_results["URL"].apply(lambda a: a.split("=")[-1])
    return auction_results


# Give the vaues in the Condition column with VIN column values somes meaning
def clean_condition_column(auction_results):
    auction_results["Condition"].replace({"Nigeria": "Cont23456"})
    return auction_results


# Give the vaues in the VIN column with Condition column values somes meaning
def clean_vin_column(auction_results):
    auction_results["VIN"].replace(
        {
            "Used": "Used_Vehicle",
            "Accidented": "Used_Vehicle",
            "0KG": "Used_Items_In_Container",
            "1,020KG": "Used_items_In_Container",
            "19,958KG": "Used_Items_In_Container",
        }
    )
    return auction_results


# Give the values in the Transmission Column some meaning
def clean_transmission_column(auction_results):
    auction_results["Transmission"].replace(
        {
            "AUTOMATIC": "Automatic_Vehicle",
            "Automatic": "Automatic_Vehicle",
            "Manual": "Manual_Vehicle",
        }
    )
    auction_results["Transmission"] = (
        auction_results["Transmission"]
        .fillna("Container_Like")
        .replace("NaN", "Container_Like")
    )
    return auction_results


# Give the values in the Mileage Column some meaning
def clean_mileage_column(auction_results):
    auction_results["Mileage"].replace({"0.00KM": "Kilometers"})
    auction_results["Mileage"] = (
        auction_results["Mileage"].fillna("None").replace("NaN", "None")
    )
    return auction_results


# Give the values in the Fuel Type Column some meaning
def clean_fuel_type_column(auction_results):
    auction_results["Fuel Type"].replace(
        {
            "Petrol": "Petrol_Vehicle",
            "PETROL": "Petrol_Vehicle",
            "NIL": "Petrol_Vehicle",
        }
    )
    auction_results.at[14, "Fuel Type"] = (
        "Diesel_Vehicle"  # Used indexing starting from 0 replacing values at specified rows
    )
    auction_results.at[18, "Fuel Type"] = "Diesel_Vehicle"
    auction_results.at[20, "Fuel Type"] = "Diesel_Vehicle"
    auction_results.at[46, "Fuel Type"] = "Diesel_Vehicle"
    auction_results.at[55, "Fuel Type"] = "Diesel_Vehicle"
    auction_results.at[71, "Fuel Type"] = "Diesel_Vehicle"
    # replace NaN with None
    auction_results["Fuel Type"] = (
        auction_results["Fuel Type"].fillna("None").replace("NaN", "None")
    )
    auction_results["Fuel Type"] = auction_results["Fuel Type"].replace(
        "('Diesel_Vehicle',)", "Diesel_Vehicle"
    )
    return auction_results


# Change Column names
def clean_the_overall_table(auction_results):
    auction_results.rename(
        columns={
            "URL": "Bidding_Item",
            "Reference Number": "Reference_Number",
            "Price": "Bid_Winning_Price",
            "Car Title": "Bidding_Item_Title",
            "Condition": "Bid_Item_Identification_Number",
            "VIN": "Condition",
            "Transmission": "Transmission_Type",
            "Fuel Type": "Fuel_Type",
        },
        inplace=True,
    )
    # set the unnamed column as an index
    auction_results.index = auction_results["Unnamed: 0"]
    # drop the unnamed column
    auction_results = auction_results.drop(["Unnamed: 0"], axis=1)
    # drop the unnamed column as an index and create a new index
    auction_results.reset_index(drop=True, inplace=True)
    return auction_results


# Was having issues changing the data type of the Bid winning
# price therefore i had to replace the naira signs and commas to empty spaces
def clean_the_price_column(auction_results):
    auction_results["Bid_Winning_Price"] = (
        auction_results["Bid_Winning_Price"]
        .replace({"₦": "", ",": ""}, regex=True)
        .astype(float)
    )
    return auction_results


# saving my table to a csv file in my desktop
def save_the_cleaned_table(auction_results):
    auction_results.to_csv(
        "C:\\Users\\HP\\Desktop\\Phyton for everybody with Dr Chuck\\Scrapped_Data\\Cleaned_Scrapped_bidding_data.csv",
        index=False,
    )
    print("Table saved")
    return auction_results
