import sys
from datetime import date, timedelta
today = date.today()
first_day = today.replace(day=1)
last_month = first_day - timedelta(days=1)
month_date = last_month.strftime("%b-%Y")
load_month = last_month.strftime("%b")
load_year = last_month.strftime("%Y")

if (sys.platform == 'win32'):
    pdf_dir = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\pdfs\\{}\\'.format(load_year)
    raw_dir = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\data\\RAW\\{}\\'.format(load_year)
    out_dir = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\data\\PUB\\{}\\'.format(load_year)
elif sys.platform == 'darwin':
    pdf_dir = '/Users/glstream/Documents/GitHub/home_prices/real_estate/pdfs/{}/'.format(load_year)
    raw_dir = '/Users/glstream/Documents/GitHub/home_prices/real_estate/data/RAW/{}/'.format(load_year)
    out_dir = '/Users/glstream/Documents/GitHub/home_prices/real_estate/data/PUB/{}/'.format(load_year)
elif sys.platform == 'linux':
    pdf_dir = '/home/pi/Documents/project-file/real_estate/pdfs/{}/'.format(load_year)
    raw_dir = '/home/pi/Documents/project-file/real_estate/data/RAW/{}/'.format(load_year)
    out_dir = '/home/pi/Documents/project-file/real_estate/data/PUB/{}/'.format(load_year)