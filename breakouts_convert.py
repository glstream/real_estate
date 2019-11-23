import csv, tabula, requests
from datetime import date, timedelta

#DECLARATIONS
file_url = "https://www.nwmls.com/library/CorporateContent/statistics/KCBreakouts.pdf"

today = date.today()
first_day = today.replace(day=1)
last_month = first_day - timedelta(days=1)
month_date = last_month.strftime("%b-%Y")
load_month = last_month.strftime("%b")

pdf_all = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\pdfs\\KCBreakouts_{}.pdf'.format(load_month)
#GET PDF FILE
r = requests.get(file_url, stream = True) 
  
with open(pdf_all,"wb") as pdf: 
    for chunk in r.iter_content(chunk_size=1024): 
         # writing one chunk at a time to pdf file 
         if chunk: 
             pdf.write(chunk)


#WRITE PDF FILE TO CSV
for page_num in range(1,4):

    pdf_dir = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\pdfs\\'
    raw_dir = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\data\\RAW\\'
    out_dir = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\data\\PUB\\'

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
    tabula.convert_into(pdf_all, raw_file, pages=str(page_num))

    #CLEAN AND PREP CSV FILE
    with open(raw_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        records = []
        for row in csv_reader:
            row2 = [r.replace('%', '').replace('"', '') for r in row]
            if len(row2[0]) == 3:
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