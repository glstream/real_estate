import mysql.connector
import sys, csv, os, sys
from datetime import date, timedelta, datetime
from priv import *  
#configs for database

db = mysql.connector.connect(
  host=host,
  user=user,
  passwd=grantPass,
  db="real_estate"
)
print('Connected to database \n')
cur = db.cursor()
enteredDateString = '{}-{}'.format(sys.argv[1], sys.argv[2])
enteredDate = datetime.strptime(enteredDateString, '%b-%Y')
load_date = enteredDate.strftime('%Y-%m-%d')

bkfl_load_month = sys.argv[1]
bkfl_load_year = sys.argv[2]
table_list = ['res, res_condo', 'condo']
if sys.platform == 'win32': 
	pub_real_dir = '.././data/PUB/{}'.format(bkfl_load_year)
elif sys.platform == 'linux':
	pub_real_dir ='/home/pi/Documents/project-file/real_estate/data/PUB/{}'.format(bkfl_load_year) 

print(pub_real_dir)

files = ['KCBreakouts_{}_CONDO.txt'.format(bkfl_load_month), 'KCBreakouts_{}_RES_CONDO.txt'.format(bkfl_load_month), 'KCBreakouts_{}_RES.txt'.format(bkfl_load_month)]

for file in files:
    target_dir = "{}/{}".format(pub_real_dir, file)
    print(target_dir)
    if 1 == 1:
        print(target_dir)
        if 'RES_CONDO.txt' in file:
            table = 'res_condo'
        elif '_RES.txt' in file:
            table = 'res'
        elif '_CONDO.txt' in file:
            table = 'condo'
        with open(target_dir, 'r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                month_year = row[0]
                region_id =  row[1]
                new_listing_curr_year = row[2]
                new_listing_prev_year = row[3]
                total_active_curr_year = row[4]
                total_active_prev_year = row[5]
                percent_chg_total_active = row[6].replace('%', '')
                pending_curr_year = row[7]
                pending_prev_year = row[8]
                percent_chg_total_pending = row[9].replace('%', '')
                closed_curr_year = row[10]
                closed_prev_year = row[11]
                percent_chg_total_closed = row[12].replace('%', '')
                median_price_curr_year = row[13].replace('$', '').replace(',', '')
                median_price_prev_year = row[14].replace('$', '').replace(',', '')
                precent_chg_median_price = row[15].replace('%', '')
                months_of_inventory = row[16] if (row[16] != '#DIV/0!' and row[16] != 'N/A') else 0.00
                
                insert_query= """
                INSERT INTO {18}_home_data_summary
                VALUES
                ('{0}','{1}','{2}',{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16}, {17})
                """.format(load_date,
                    month_year,
                region_id,
                int(new_listing_curr_year),
                int(new_listing_prev_year),
                int(total_active_curr_year),
                int(total_active_prev_year),
                float(percent_chg_total_active),
                int(pending_curr_year),
                int(pending_prev_year),
                float(percent_chg_total_pending),
                int(closed_curr_year),
                int(closed_prev_year),
                float(percent_chg_total_closed),
                int(median_price_curr_year),
                int(median_price_prev_year),
                float(precent_chg_median_price),
                months_of_inventory,
                table)

                print(insert_query)
                cur.execute(insert_query)
                db.commit()
                # print("records commited: {}").format(row)
db.close()

