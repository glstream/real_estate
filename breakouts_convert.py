import csv, tabula, requests, sys
from datetime import date, timedelta
from OS_NAME_PATHS import *

#DECLARATIONS
file_url = "https://www.nwmls.com/library/CorporateContent/statistics/KCBreakouts.pdf"

today = date.today()
first_day = today.replace(day=1)
last_month = first_day - timedelta(days=1)
month_date = last_month.strftime("%b-%Y")
load_month = last_month.strftime("%b")
load_year = last_month.strftime("%Y")

r = requests.get(file_url, stream = True) 

if sys.platform == 'win32':
    pdf_all = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\pdfs\\{0}\\KCBreakouts_{1}.pdf'.format(load_year,load_month) 
elif sys.platform == 'darwin':
    pdf_all = "/Users/glstream/Documents/GitHub/home_prices/real_estate/pdfs/{0}/KCBreakouts_{1}.pdf".format(load_year,load_month)
elif sys.platform == 'linux':
    pdf_all  = "/home/pi/Documents/project-file/real_estate/pdfs/{0}/KCBreakouts_{1}.pdf".format(load_year, load_month)  
#GET PDF FILE
r = requests.get(file_url, stream = True) 
  
with open(pdf_all,"wb") as pdf: 
    for chunk in r.iter_content(chunk_size=1024): 
         # writing one chunk at a time to pdf file 
         if chunk: 
             pdf.write(chunk)


#WRITE PDF FILE TO CSV
for page_num in range(1,4):

    pdf_dir = '{}'.format(pdf_dir)
    raw_dir = raw_dir
    out_dir = out_dir

    if page_num == 1:
        pdf_file = "KCBreakouts_{}_RES_CONDO.pdf".format(load_month)
        raw =  "RAW_KCBreakouts_{}_RES_CONDO.txt".format(load_month)
        out = "KCBreakouts_{}_RES_CONDO.txt".format(load_month)
    elif page_num == 2:
        pdf_file =  "KCBreakouts_{}_RES.pdf".format(load_month)
        raw = "RAW_KCBreakouts_{}_RES.txt".format(load_month)
        out = "KCBreakouts_{}_RES.txt".format(load_month)
    else: 
        pdf_file = "KCBreakouts_{}_CONDO.pdf".format(load_month)
        raw =  "RAW_KCBreakouts_{}_CONDO.txt".format(load_month)
        out = "KCBreakouts_{}_CONDO.txt".format(load_month)
    
    pdf_part_file = pdf_dir + pdf_file
    raw_file = raw_dir + raw
    out_file = out_dir + out

    # tables = tabula.read_pdf(pdf_all, pages = str(page_num), multiple_tables = True)
    tabula.convert_into(pdf_all, raw_file, lattice=True, output_format="csv", pages=str(page_num))

    #CLEAN AND PREP CSV FILE
    with open(raw_file, 'r') as csv_file:
        print(raw_file)
        csv_reader = csv.reader(csv_file, delimiter=',')
        records = []
        for row in csv_reader:
            print(row)
            row2 = [r.replace('%', '').replace('"', '') for r in row]
            print('row2', row2)
            if len(row2[0]) == 3:
                print(row2)
                row2.insert(0,month_date)
                # row = [r.replace('%', '').replace('"', '') for r in row]
                records.append(row2)
                # print(type(row[0]), len(row[0]),row[0])
                # print(row)
    #WRITE PREPED DATA TO FILE
    with open(out_file, mode='w', newline='') as real_estate_file:
        realestate_writer = csv.writer(real_estate_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in records:
            realestate_writer.writerow(row)


