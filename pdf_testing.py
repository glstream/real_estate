import csv, tabula
from datetime import date, timedelta

pdf_in_file = '/Users/gstream/Documents/ST/playground/pdf_breakouts/pdfs/TEST.pdf'
raw_file = '/Users/gstream/Documents/ST/playground/pdf_breakouts/data/RAW/RAW_TEST.txt'


today = date.today()
first_day = today.replace(day=1)
last_month = first_day - timedelta(days=1)
month_date = last_month.strftime("%b-%Y")



tables = tabula.read_pdf(pdf_in_file, pages = "2", multiple_tables = True)
tabula.convert_into(pdf_in_file, raw_file, pages="2")