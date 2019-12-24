import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter,FuncFormatter, StrMethodFormatter
import numpy as np
import math, os, pathlib
from datetime import date, timedelta
from twython import Twython
from auth import *
from OS_NAME_PATHS import *


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

today = date.today()
first_day = today.replace(day=1)
last_month = first_day - timedelta(days=1)
load_month_date = last_month.strftime("%b_%Y")
display_month_date = last_month.strftime("%B-%Y")


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

def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        height_string = str(round(height, -3))[:3] if height < 1000000 else str(round(height, -3))[:4]
        ax.annotate('{}K'.format(height_string),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', 
                    va='bottom',
                    size=8)
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

table_list = [['res', 'Residential', 'SFH'], ['res_condo', 'Mixed', 'SFH/Condo'], ['condo', 'Condo', 'Condo']]

for table in table_list:
    #     #query for database
    viz_query= """
    select  month_year, dr.region_name, median_price_curr_year, median_price_prev_year
    from {0}_home_data_summary rs
    inner join dim_regions dr on rs.region_id = dr.region_id
    where 1=1
    order by load_date asc""".format(table[0])
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



    labels = df['Date'].unique().tolist()
    x = np.arange(len(labels))  # the label locations
    width= 0.35

    #WEST SEATTLE
    is_w_seattle = df['Region'] == 'W Seattle'
    w_seattle_df = df[is_w_seattle]
    w_seattle_curr_year_median = w_seattle_df['MedianPrice'].tolist()
    w_seattle_last_year_median = w_seattle_df['LastYearMedianPrice'].tolist()
    w_seattle_low = min(w_seattle_last_year_median) if (min(w_seattle_curr_year_median) > min(w_seattle_last_year_median)) else min(w_seattle_curr_year_median)
    w_seattle_high = max(w_seattle_last_year_median) if (max(w_seattle_curr_year_median) < max(w_seattle_last_year_median)) else max(w_seattle_curr_year_median)

    #N Seattle 
    is_n_seattle = df['Region'] == 'N Seattle'
    n_seattle_df = df[is_w_seattle]
    n_seattle_curr_year_median = n_seattle_df['MedianPrice'].tolist()
    n_seattle_last_year_median = n_seattle_df['LastYearMedianPrice'].tolist()
    n_seattle_low = min(n_seattle_last_year_median) if (min(n_seattle_curr_year_median) > min(n_seattle_last_year_median)) else min(n_seattle_curr_year_median)
    n_seattle_high = max(n_seattle_last_year_median) if (max(n_seattle_curr_year_median) < max(n_seattle_last_year_median)) else max(n_seattle_curr_year_median)

    # Central Seattle SE, Leshi, Mt Baker 
    is_se_seattle = df['Region'] == 'Central Seattle SE, Leshi, Mt Baker'
    se_seattle_df = df[is_se_seattle]
    se_seattle_curr_year_median = se_seattle_df['MedianPrice'].tolist()
    se_seattle_last_year_median = se_seattle_df['LastYearMedianPrice'].tolist()
    se_seattle_low = min(se_seattle_last_year_median) if (min(se_seattle_curr_year_median) > min(se_seattle_last_year_median)) else min(se_seattle_curr_year_median)
    se_seattle_high = max(se_seattle_last_year_median) if (max(se_seattle_curr_year_median) < max(se_seattle_last_year_median)) else max(se_seattle_curr_year_median)

    # Queen Anne   
    is_qa_seattle = df['Region'] == 'Queen Anne'
    qa_seattle_df = df[is_qa_seattle]
    qa_seattle_curr_year_median = qa_seattle_df['MedianPrice'].tolist()
    qa_seattle_last_year_median = qa_seattle_df['LastYearMedianPrice'].tolist()
    qa_seattle_low = min(qa_seattle_last_year_median) if (min(qa_seattle_curr_year_median) > min(qa_seattle_last_year_median)) else min(qa_seattle_curr_year_median)
    qa_seattle_high = max(qa_seattle_last_year_median) if (max(qa_seattle_curr_year_median) < max(qa_seattle_last_year_median)) else max(qa_seattle_curr_year_median)

    # Central Seattle SW, Beacon Hill    
    is_sw_seattle = df['Region'] == 'Central Seattle SW, Beacon Hill'
    sw_seattle_df = df[is_sw_seattle]
    sw_seattle_curr_year_median = sw_seattle_df['MedianPrice'].tolist()
    sw_seattle_last_year_median = sw_seattle_df['LastYearMedianPrice'].tolist()
    sw_seattle_low = min(sw_seattle_last_year_median) if (min(sw_seattle_curr_year_median) > min(sw_seattle_last_year_median)) else min(sw_seattle_curr_year_median)
    sw_seattle_high = max(sw_seattle_last_year_median) if (max(sw_seattle_curr_year_median) < max(sw_seattle_last_year_median)) else max(sw_seattle_curr_year_median)

    # Ballard, Greenlake    
    is_bg_seattle = df['Region'] == 'Ballard, Greenlake'
    bg_seattle_df = df[is_bg_seattle]
    bg_seattle_curr_year_median = bg_seattle_df['MedianPrice'].tolist()
    bg_seattle_last_year_median = bg_seattle_df['LastYearMedianPrice'].tolist()
    bg_seattle_low = min(bg_seattle_last_year_median) if (min(bg_seattle_curr_year_median) > min(bg_seattle_last_year_median)) else min(bg_seattle_curr_year_median)
    bg_seattle_high = max(bg_seattle_last_year_median) if (max(bg_seattle_curr_year_median) < max(bg_seattle_last_year_median)) else max(bg_seattle_curr_year_median)

    #Central Seattle, Capitol Hill
    is_ch_seattle = df['Region'] == 'Central Seattle, Capitol Hill'
    ch_seattle_df = df[is_ch_seattle]
    ch_seattle_curr_year_median = ch_seattle_df['MedianPrice'].tolist()
    ch_seattle_last_year_median = ch_seattle_df['LastYearMedianPrice'].tolist()
    ch_seattle_low = min(ch_seattle_last_year_median) if (min(ch_seattle_curr_year_median) > min(ch_seattle_last_year_median)) else min(ch_seattle_curr_year_median)
    ch_seattle_high = max(ch_seattle_last_year_median) if (max(ch_seattle_curr_year_median) < max(ch_seattle_last_year_median)) else max(ch_seattle_curr_year_median)

    fig = plt.figure(figsize=(10,8))

    #WEST SEATTLE
    ax1 = fig.add_subplot(4, 2, 1, xticklabels=labels,fc="white",)
    rects1 = ax1.bar(x + width/2, 
                            w_seattle_curr_year_median, 
                            width, 
                            color="blue",
                            edgecolor="black", 
                            alpha=.8,
                            label='Current Year')

    rects1b = ax1.bar(x - width/2, 
                            w_seattle_last_year_median, 
                            width, 
                            color="gray",
                            edgecolor="black", 
                            alpha=.7,
                            label='Previous Year')
    ax1.set_xticks(x)
    ax1.xaxis.set_ticklabels(labels,size=8)
    ax1.yaxis.set_ticklabels(labels,size=8)

    # ax1.set_xticklabels(labels, size=6)
    autolabel(rects1, ax1)
    autolabel(rects1b, ax1)
    w_high = math.ceil(w_seattle_high+0.5*(w_seattle_high-w_seattle_low))
    w_low = math.ceil(w_seattle_low-0.5*(w_seattle_high-w_seattle_low))
    w_low = w_low if w_low > 0 else 0

    ax1.set_ylim([w_low, w_high])
    ax1.yaxis.set_major_formatter(FuncFormatter(format_tick_labels))
    ax1.set_title('West Seattle Median {0} Prices by Month'.format(table[2]),  fontname="DejaVu Sans", fontsize=10)

    #SE SEATTLE
    ax2 = fig.add_subplot(4, 2, 2, xticklabels=labels,fc="white",)
    rects2 = ax2.bar(x + width/2, 
                            se_seattle_curr_year_median, 
                            width, 
                            color="blue",
                            edgecolor="black", 
                            alpha=.8,
                            label='Current Year')

    rects2b = ax2.bar(x - width/2, 
                            se_seattle_last_year_median, 
                            width, 
                            color="gray",
                            edgecolor="black", 
                            alpha=.7,
                            label='Previous Year')
    ax2.set_xticks(x)
    ax2.xaxis.set_ticklabels(labels,size=8)
    ax2.yaxis.set_ticklabels(labels,size=8)
    autolabel(rects2, ax2)
    autolabel(rects2b, ax2)

    se_high = math.ceil(se_seattle_high+0.5*(se_seattle_high-se_seattle_low))
    se_low = math.ceil(se_seattle_low-0.5*(se_seattle_high-se_seattle_low))
    se_low = se_low if se_low > 0 else 0
    ax2.set_ylim([se_low, se_high])

    ax2.yaxis.set_major_formatter(FuncFormatter(format_tick_labels))
    ax2.set_title('SE Seattle Median {0} Prices by Month'.format(table[2]),  fontname="DejaVu Sans", fontsize=10)


    #Central Seattle, Capitol Hill
    ax3 = fig.add_subplot(4, 2, 3, xticklabels=labels,fc="white",)
    rects3 = ax3.bar(x + width/2, 
                            ch_seattle_curr_year_median, 
                            width, 
                            color="blue",
                            edgecolor="black", 
                            alpha=.8,
                            label='Current Year')

    rects3b = ax3.bar(x - width/2, 
                            ch_seattle_last_year_median, 
                            width, 
                            color="gray",
                            edgecolor="black", 
                            alpha=.7,
                            label='Previous Year')
    ax3.set_xticks(x)
    ax3.xaxis.set_ticklabels(labels,size=8)
    ax3.yaxis.set_ticklabels(labels,size=8)

    autolabel(rects3, ax3)
    autolabel(rects3b, ax3)

    ch_high = math.ceil(ch_seattle_high+0.5*(ch_seattle_high-ch_seattle_low))
    ch_low = math.ceil(ch_seattle_low-0.5*(ch_seattle_high-ch_seattle_low))
    ch_low = ch_low if ch_low > 0 else 0

    ax3.set_ylim([ch_low, ch_high])
    ax3.yaxis.set_major_formatter(FuncFormatter(format_tick_labels))
    ax3.set_title('Central Seattle, Capitol Hill Median {} Prices by Month'.format(table[2]),  fontname="DejaVu Sans", fontsize=10)


    # Queen Anne 
    ax4 = fig.add_subplot(4, 2, 4, xticklabels=labels,fc="white",)
    rects4 = ax4.bar(x + width/2, 
                            qa_seattle_curr_year_median, 
                            width, 
                            color="blue",
                            edgecolor="black", 
                            alpha=.8,
                            label='Current Year')

    rects4b = ax4.bar(x - width/2, 
                            qa_seattle_last_year_median, 
                            width, 
                            color="gray",
                            edgecolor="black", 
                            alpha=.7,
                            label='Previous Year')
    ax4.set_xticks(x)
    ax4.xaxis.set_ticklabels(labels,size=8)
    ax4.yaxis.set_ticklabels(labels,size=8)
    autolabel(rects4, ax4)
    autolabel(rects4b, ax4)

    qa_high = math.ceil(qa_seattle_high+0.5*(qa_seattle_high-qa_seattle_low))
    qa_low = math.ceil(qa_seattle_low-0.5*(qa_seattle_high-qa_seattle_low))
    qa_low = qa_low if qa_low > 0 else 0

    ax4.set_ylim([qa_low, qa_high])
    ax4.yaxis.set_major_formatter(FuncFormatter(format_tick_labels))
    ax4.set_title('Queen Anne Median {0} Prices by Month'.format(table[2]),  fontname="DejaVu Sans", fontsize=10)

    # Ballard, Greenlake
    ax5 = fig.add_subplot(4, 2, 5, xticklabels=labels,fc="white",)
    rects5 = ax5.bar(x + width/2, 
                            bg_seattle_curr_year_median, 
                            width, 
                            color="blue",
                            edgecolor="black", 
                            alpha=.8,
                            label='Current Year')

    rects5b = ax5.bar(x - width/2, 
                            bg_seattle_last_year_median, 
                            width, 
                            color="gray",
                            edgecolor="black", 
                            alpha=.7,
                            label='Previous Year')
    ax5.set_xticks(x)
    ax5.xaxis.set_ticklabels(labels,size=8)
    ax5.yaxis.set_ticklabels(labels,size=8)
    autolabel(rects5, ax5)
    autolabel(rects5b, ax5)

    bg_high = math.ceil(bg_seattle_high+0.5*(bg_seattle_high-bg_seattle_low))
    bg_low = math.ceil(bg_seattle_low-0.5*(bg_seattle_high-bg_seattle_low))
    bg_low = bg_low if bg_low > 0 else 0

    ax5.set_ylim([bg_low, bg_high])
    ax5.yaxis.set_major_formatter(FuncFormatter(format_tick_labels))
    ax5.set_title('Ballard/Greenlake Median {0} Prices by Month'.format(table[2]),  fontname="DejaVu Sans", fontsize=10)

    #North SEATTLE
    ax6 = fig.add_subplot(4, 2, 6, xticklabels=labels,fc="white",)
    rects6 = ax6.bar(x + width/2, 
                            n_seattle_curr_year_median, 
                            width, 
                            color="blue",
                            edgecolor="black", 
                            alpha=.8,
                            label='Current Year')

    rects6b = ax6.bar(x - width/2, 
                            n_seattle_last_year_median, 
                            width, 
                            color="gray",
                            edgecolor="black", 
                            alpha=.7,
                            label='Previous Year')
    ax6.set_xticks(x)
    ax6.xaxis.set_ticklabels(labels,size=8)
    ax6.yaxis.set_ticklabels(labels,size=8)
    autolabel(rects6, ax6)
    autolabel(rects6b, ax6)

    n_high = math.ceil(n_seattle_high+0.5*(n_seattle_high-n_seattle_low))
    n_low = math.ceil(n_seattle_low-0.5*(n_seattle_high-n_seattle_low))
    n_low = n_low if n_low > 0 else 0

    ax6.set_ylim([n_low, n_high])
    ax6.yaxis.set_major_formatter(FuncFormatter(format_tick_labels))
    ax6.set_title('North Seattle Median {} Prices by Month'.format(table[2]),  fontname="DejaVu Sans", fontsize=10)
    
    #SW SEATTLE
    ax7 = fig.add_subplot(4, 2, 7, xticklabels=labels,fc="white",)
    rects7 = ax7.bar(x + width/2, 
                            sw_seattle_curr_year_median, 
                            width, 
                            color="blue",
                            edgecolor="black", 
                            alpha=.8,
                            label='Current Year')

    rects7b = ax7.bar(x - width/2, 
                            sw_seattle_last_year_median, 
                            width, 
                            color="gray",
                            edgecolor="black", 
                            alpha=.7,
                            label='Previous Year')
    ax7.set_xticks(x)
    ax7.xaxis.set_ticklabels(labels,size=8)
    ax7.yaxis.set_ticklabels(labels,size=8)
    autolabel(rects7, ax7)
    autolabel(rects7b, ax7)

    sw_high = math.ceil(sw_seattle_high+0.5*(sw_seattle_high-sw_seattle_low))
    sw_low = math.ceil(sw_seattle_low-0.5*(sw_seattle_high-sw_seattle_low))
    sw_low = sw_low if sw_low > 0 else 0

    ax7.set_ylim([sw_low, sw_high])
    ax7.yaxis.set_major_formatter(FuncFormatter(format_tick_labels))
    ax7.set_title('SW Seattle Median {0} Prices by Month'.format(table[2]),  fontname="DejaVu Sans", fontsize=10)
    
    ax7.legend(bbox_to_anchor=(1., 1, 1., .12), loc='lower left',
                ncol=2, mode="expand", borderaxespad=0.2)


    plt.tight_layout()
    # plt.show()
    vizfile = '{0}_{1}.png'.format(table[0], load_month_date)
    print(pathlib.Path(viz_dir, vizfile))
    fig.savefig(pathlib.Path(viz_dir, vizfile), dpapi=1200)
    full_file = pathlib.Path(viz_dir, vizfile)
    
    #TWEETING IMAGE
    # formatted_message = """{0}\nMedian {1}  by Month
    #                     #Seattle #seattlerealestate #realestate""".format(display_month_date, table[2])
    # image = open(full_file, 'rb')
    # response = twitter.upload_media(media=image)

    # twitter.update_status(status=formatted_message, media_ids=[response['media_id']])
    # print("Tweeted: {}".format(formatted_message))
db.close()