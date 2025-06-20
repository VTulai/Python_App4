import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path


output_path = "PDF/"
files = []
Path(output_path).mkdir(exist_ok=True)

def read_excel_data(folder_path="invoices"):
    all_files = glob.glob(f"{folder_path}/*.xlsx")

    for file in all_files:
        files.append(pd.read_excel(file, sheet_name="Sheet 1"))
        name, date = extract_invoice_number(file)
        create_pdf(name, date)

def create_pdf(name, date):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=50, h=12, txt=f"Invoice nr. {name}", align="L", ln=1)
    pdf.cell(w=50, h=12, txt=f"Date {date}", align="L", ln=1)
    pdf.output(f"{output_path}{name}-{date}.pdf")

def extract_invoice_number(path_to_xlsx_file):
    file_name = Path(path_to_xlsx_file).stem
    name, date = file_name.split('-')
    return name, date

read_excel_data()
print(files)