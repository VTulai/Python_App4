import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path

from pandas._typing import IntStrT
from pandas.core.interchange.dataframe_protocol import DataFrame

output_path = "PDF/"
Path(output_path).mkdir(exist_ok=True)
folder_path="invoices"

def extract_invoice_number(path_to_xlsx_file):
    file_name = Path(path_to_xlsx_file).stem
    name, date = file_name.split('-')
    return name, date


all_files = glob.glob(f"{folder_path}/*.xlsx")

for file in all_files:
    excel_data = pd.read_excel(file, sheet_name="Sheet 1")
    name, date = extract_invoice_number(file)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=50, h=12, txt=f"Invoice nr. {name}", align="L", ln=1)
    pdf.cell(w=50, h=12, txt=f"Date {date}", align="L", ln=1)

    columns_list = excel_data.columns
    columns_list = [item.replace("_", " ").title() for item in columns_list]
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=30, h=12, txt=f"{columns_list[0]}", align="C", border=1)
    pdf.cell(w=60, h=12, txt=f"{columns_list[1]}", align="C", border=1)
    pdf.cell(w=40, h=12, txt=f"{columns_list[2]}", align="C", border=1)
    pdf.cell(w=30, h=12, txt=f"{columns_list[3]}", align="C", border=1)
    pdf.cell(w=30, h=12, txt=f"{columns_list[4]}", align="C", border=1, ln=1)

    for index, row in excel_data.iterrows():
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=30, h=12, txt=f"{row['product_id']}", align="C", border=1)
        pdf.cell(w=60, h=12, txt=f"{row['product_name']}", align="C", border=1)
        pdf.cell(w=40, h=12, txt=f"{row['amount_purchased']}", align="C", border=1)
        pdf.cell(w=30, h=12, txt=f"{row['price_per_unit']}", align="C", border=1)
        pdf.cell(w=30, h=12, txt=f"{row['total_price']}", align="C", border=1, ln=1)

    total_amount = sum(excel_data['total_price'])

    pdf.set_font(family="Times", size=12)
    pdf.cell(w=30, h=12, align="C", border=1)
    pdf.cell(w=60, h=12, align="C", border=1)
    pdf.cell(w=40, h=12, align="C", border=1)
    pdf.cell(w=30, h=12, align="C", border=1)
    pdf.cell(w=30, h=12, txt=f"{total_amount}", align="C", border=1, ln=1)

    pdf.set_font(family="Times", size=14)
    pdf.cell(w=0, h=12, txt=f"The total due amount is {total_amount} Euros", align="L", ln=1)
    pdf.cell(w=25, h=12, txt=f"PythonHow")
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"{output_path}{name}-{date}.pdf")
