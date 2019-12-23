import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter,FuncFormatter, StrMethodFormatter
import numpy as np
import math, os
from auth import *
from OS_NAME_PATHS import *


def format_tick_labels(x, pos):
    """Format hundereds of K"""
    if x >= 1000000:
        x = str(round(int(x),-4))
        x = '${}K'.format(x[0:4])
        return x
    elif x < 999999:
        x = str(round(int(x),-4))
        x = '${}K'.format(x[0:3])
        return x

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        height_string = str(round(height, -3))[:3] if height < 1000000 else str(round(height, -3))[:4]
        ax.annotate('{}K'.format(height_string),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', 
                    va='bottom')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

#Auth for DB connection
db = mysql.connector.connect(
  host=host,
  user=user,
  passwd=grantPass,
  db="real_estate"
)

print('Connected to database \n')
cur = db.cursor()
regions = ['W Seattle','Central Seattle SE, Leshi, Mt Baker','Central Seattle SW, Beacon Hill','Central Seattle, Capitol Hill','Queen Anne','Ballard, Greenlake','N Seattle']
table_list = [['res', 'Residential'], ['res_condo', 'Residential/Condo'], ['condo', 'Condo']]

for table in table_list:
    for region in regions:
        #query for database
        viz_query= """
        select  month_year, dr.region_name, median_price_curr_year, median_price_prev_year
        from {0}_home_data_summary rs
        inner join dim_regions dr on rs.region_id = dr.region_id
        where 1=1
        and region_name = '{1}'
        order by load_date asc""".format(table[0],region)
        #execution query and return of each record represented as a tuple
        cur.execute(viz_query)
        rows = cur.fetchall()
        # Create target Directory if don't exist
        if not os.path.exists(viz_dir):
            os.makedirs(viz_dir)
            print("Directory {} Created".format(viz_dir))
        else:    
            print("Directory {} Created".format(viz_dir))
        
        #change the tuple return to 
        df = pd.DataFrame( [[ij for ij in i] for i in rows] )
        df.rename(columns={0: 'Date', 1: 'Region', 2: 'MedianPrice', 3: 'LastYearMedianPrice'}, inplace=True);
        # print(df['MedianPrice'].max())

        labels = df['Date'].values.tolist()
        curr_year_median = df['MedianPrice'].values.tolist()
        last_year_median = df['LastYearMedianPrice'].values.tolist()

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x + width/2, 
                        curr_year_median, 
                        width, 
                        color="blue",
                        edgecolor="black", 
                        alpha=.7,
                        label='Current Year')

        rects2 = ax.bar(x - width/2, 
                        last_year_median, 
                        width, 
                        color="gray",
                        edgecolor="black",
                        alpha=.4,
                        label='Previous Year')

        #  Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Median Price', fontname="Arial", fontsize=8)
        ax.set_title('{0} {1} Median Home Prices by Month'.format(region,table[1]),  fontname="DejaVu Sans", fontsize=10)


        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        autolabel(rects1)
        autolabel(rects2)
        low = min(last_year_median) if (min(curr_year_median) > min(last_year_median)) else min(curr_year_median)
        print('low', low, region)
        high = max(last_year_median) if (max(curr_year_median) < max(last_year_median)) else max(curr_year_median)
        print('high', high, region)
        plt.ylim([math.ceil(low-0.5*(high-low)), math.ceil(high+0.5*(high-low))])
        
        ax.yaxis.set_major_formatter(FuncFormatter(format_tick_labels))

        fig.savefig('{0}{1}_{2}'.format(viz_dir,table[0],region.replace(" ", '').replace(",", "_")))
db.close()