import glob

import pandas as pd

files = []

def read_excel_data(folder_path="invoices"):
    all_files = glob.glob(f"{folder_path}/*.xlsx")

    for file in all_files:
        files.append(pd.read_excel(file, sheet_name="Sheet 1"))