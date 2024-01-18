import os
import requests
import pandas as pd

api_url = "http://localhost:5001/products"

def get_api_data():
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Error obtaining data from the API. Status: {response.status_code}")
    print(f"Status: {response.status_code}")
    return response.json()

def convert_to_excel(data):
    dataframe = pd.DataFrame(data["products"])
    excel_path = os.path.expanduser("~/Downloads/products_data.xlsx")
    dataframe.to_excel(excel_path, index=False)
    return excel_path

try:
    api_data = get_api_data()
    saved_excel_file_path = convert_to_excel(api_data)
    print(f"Data converted to '.xlsx'. File saved at: {saved_excel_file_path}")
except Exception as e:
    print(f"Error: {e}")
