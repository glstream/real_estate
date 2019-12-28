import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from auth import *

#Auth for DB connection
db = mysql.connector.connect(
  host=host,
  user=user,
  passwd=grantPass,
  db="real_estate"
)

print('Connected to database \n')
cur = db.cursor()

viz_query= """
    select 
month_year
,dm.region_name
,rh.closed_curr_year
,rh.closed_prev_year 
from res_home_data_summary rh 
inner join dim_regions dm on rh.region_id = dm.region_id""".format()

cur.execute(viz_query)

rows = cur.fetchall()
# print('ROWS:', rows)
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'Date', 1: 'Region', 2: 'MedianPrice', 3: 'LastYearMedianPrice'}, inplace=True)

labels = df['Date'].unique().tolist()

print(labels)
x = np.arange(len(labels))  # the label locations
width= 0.35
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
fig = plt.figure(figsize=(9,3))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(131)
plt.scatter(names, values, color="gray")
plt.subplot(131)
plt.plot(names, values, color="green")
plt.suptitle('Categorical Plotting')
plt.show()

plt.show()