import mysql.connector
import sys, csv, os
from datetime import date, timedelta
from priv import *  
#configs for database

db = mysql.connector.connect(
  host=host,
  user=user,
  passwd=pass,
  db="real_estate"
)
print('Connected to database \n')
cur = db.cursor()

today = date.today()
first_day = today.replace(day=1)
last_month = first_day - timedelta(days=1)
month_date = last_month.strftime("%b-%Y")
load_month = last_month.strftime("%b")

print(load_month)
table_list = ['res, res_condo', 'condo']
pub_real_dir = '.././data/PUB/'
files = ['KCBreakouts_Sep_CONDO.txt', 'KCBreakouts_Sep_RES_CONDO.txt', 'KCBreakouts_Sep_RES.txt']

for file in files:
    target_dir = "{}/{}".format(pub_real_dir, file)
    print(target_dir)
    if load_month not in target_dir:
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
                percent_chg_total_active = row[6]
                pending_curr_year = row[7]
                pending_prev_year = row[8]
                percent_chg_total_pending = row[9]
                closed_curr_year = row[10]
                closed_prev_year = row[11]
                percent_chg_total_closed = row[12]
                median_price_curr_year = row[13]
                median_price_prev_year = row[14]
                precent_chg_median_price = row[15]
                months_of_inventory = row[16]
                
                insert_query= """
                INSERT INTO {17}_home_data_summary
                VALUES
                ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}')
                """.format(month_year,
                region_id,
                new_listing_curr_year,
                new_listing_prev_year,
                total_active_curr_year,
                total_active_prev_year,
                percent_chg_total_active,
                pending_curr_year,
                pending_prev_year,
                percent_chg_total_pending,
                closed_curr_year,
                closed_prev_year,
                percent_chg_total_closed,
                median_price_curr_year,
                median_price_prev_year,
                precent_chg_median_price,
                months_of_inventory,
                table)

                print(insert_query)
                cur.execute(insert_query)
                db.commit()
                # print("records commited: {}").format(row)
db.close()
