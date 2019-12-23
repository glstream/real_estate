import sys
from datetime import date, timedelta
today = date.today()
first_day = today.replace(day=1)
last_month = first_day - timedelta(days=1)
month_date = last_month.strftime("%b-%Y")
load_month = last_month.strftime("%b")
load_year = last_month.strftime("%Y")

if (sys.platform == 'win32'):
    viz_dir = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\viz\\{0}\\{1}\\'.format(load_year,load_month)
elif sys.platform == 'darwin':
    viz_dir = '/Users/glstream/Documents/GitHub/home_prices/real_estate/pdfs/{0}/{1}'.format(load_year,load_month)
elif sys.platform == 'linux':
    viz_dir = '/home/pi/Documents/project-file/real_estate/pdfs/{0}/{1}'.format(load_year, load_month)
