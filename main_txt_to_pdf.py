import glob
from fpdf import FPDF
from pathlib import Path

output_path = "PDF_HT_4/"
Path(output_path).mkdir(exist_ok=True)
pdf = FPDF()

def read_txt_data(folder_path="txt"):
    all_files = glob.glob(f"{folder_path}/*.txt")

    for file in all_files:
        with open(file) as f:
            name = Path(file).stem
            text = f.read()
            create_pdf(name, text)

    pdf.output(f"{output_path}output.pdf")

def create_pdf(name, text):
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=50, h=12, txt=f"{name.capitalize()}", align="L", ln=1)
    pdf.set_font(family="Times", size=14)
    pdf.multi_cell(w=0, h=5, txt=f"{text}", align="L")

read_txt_data()