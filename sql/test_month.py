from datetime import date, datetime
import sys

t1 = date.today().replace(day=1).strftime('%m/%d/%y')

# t2 = datetime.strptime(t1, '%Y-%m-%d').strftime('%m/%d/%y')
date1 = '{}-{}'.format(sys.argv[1], sys.argv[2])
t3 = datetime.strptime(date1, '%b-%Y')
load_date = t3.strftime('%Y-%m-%d')
print(load_date)