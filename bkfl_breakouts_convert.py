#WRITE PDF FILE TO CSV
import csv, tabula

bkfl_year_months = [['Jul', 'Jul-2019'],['Aug', 'Aug-2019'],['Sep', 'Sep-2019'], ['Oct', 'Oct-2019']]

year_month = 'Sep'
month_date = 'Sep-2019'

for year_month in bkfl_year_months:

    if sys.platform == 'win32':
        pdf_all = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\pdfs\\KCBreakouts_{}.pdf'.format(year_month[0]) 
    elif sys.platform == 'darwin':
        pdf_all = "/Users/glstream/Documents/GitHub/home_prices/real_estate/pdfs/KCBreakouts_{}.pdf".format(year_month[0])
    elif sys.platform == 'linux':
        pdf_all  = "/home/pi/Documents/project-file/real_estate/pdfs/KCBreakouts_{}.pdf".format(year_month[0])  

    for page_num in range(1,4):

        pdf_dir = pdf_dir
        raw_dir = raw_dir
        out_dir = out_dir

        if page_num == 1:
            pdf_file = "KCBreakouts_{}_RES_CONDO.pdf".format(year_month[0])
            raw =  "RAW_KCBreakouts_{}_RES_CONDO.txt".format(year_month[0])
            out = "KCBreakouts_{}_RES_CONDO.txt".format(year_month[0])
        elif page_num == 2:
            pdf_file =  "KCBreakouts_{}_RES.pdf".format(year_month[0])
            raw = "RAW_KCBreakouts_{}_RES.txt".format(year_month[0])
            out = "KCBreakouts_{}_RES.txt".format(year_month[0])
        else: 
            pdf_file = "KCBreakouts_{}_CONDO.pdf".format(year_month[0])
            raw =  "RAW_KCBreakouts_{}_CONDO.txt".format(year_month[0])
            out = "KCBreakouts_{}_CONDO.txt".format(year_month[0])
        
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
                    row2.insert(0,year_month[1])
                    records.append(row2)

        #WRITE PREPED DATA TO FILE
        with open(out_file, mode='w', newline='') as real_estate_file:
            realestate_writer = csv.writer(real_estate_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in records:
                realestate_writer.writerow(row)