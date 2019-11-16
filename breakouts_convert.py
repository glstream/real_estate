import csv, tabula, requests
from datetime import date, timedelta

#DECLARATIONS
file_url = "https://www.nwmls.com/library/CorporateContent/statistics/KCBreakouts.pdf"
pdf_in_file = '/Users/gstream/Documents/ST/playground/pdf_breakouts/pdfs/KCBreakouts_NOV.pdf'
raw_file = '/Users/gstream/Documents/ST/playground/pdf_breakouts/data/RAW/RAW_KCBreakouts_NOV.txt'
out_file = '/Users/gstream/Documents/ST/playground/pdf_breakouts/data/PUB/KCBreakouts_NOV.txt'

today = date.today()
first_day = today.replace(day=1)
last_month = first_day - timedelta(days=1)
month_date = last_month.strftime("%b-%Y")

#GET PDF FILE
r = requests.get(file_url, stream = True) 
  
with open(pdf_in_file,"wb") as pdf: 
    for chunk in r.iter_content(chunk_size=1024): 
         # writing one chunk at a time to pdf file 
         if chunk: 
             pdf.write(chunk)


#WRITE PDF FILE TO CSV

tables = tabula.read_pdf(pdf_in_file, pages = "2", multiple_tables = True)
tabula.convert_into(pdf_in_file, raw_file, pages="2")

#CLEAN AND PREP CSV FILE
with open(raw_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    records = []
    for row in csv_reader:

        if len(row[0]) == 3:
            row.insert(0,month_date)
            records.append(row)
            # print(type(row[0]), len(row[0]),row[0])
            # print(row)

#WRITE PREPED DATA TO FILE
with open(out_file, mode='w') as real_estate_file:
    realestate_writer = csv.writer(real_estate_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in records:
        realestate_writer.writerow(row)