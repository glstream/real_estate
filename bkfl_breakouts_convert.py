#WRITE PDF FILE TO CSV
import csv, tabula



load_month = 'Sep'
month_date = 'Sep-2019'
pdf_all = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\pdfs\\KCBreakouts_{}.pdf'.format(load_month)

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
                records.append(row2)

    #WRITE PREPED DATA TO FILE
    with open(out_file, mode='w', newline='') as real_estate_file:
        realestate_writer = csv.writer(real_estate_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in records:
            realestate_writer.writerow(row)