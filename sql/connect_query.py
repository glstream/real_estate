import mysql.connector
import sys, csv, os
from datetime import date, timedelta
from priv import *
#configs for database

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=grantPass,
  db="real_estate"
)
print('Connected to database \n')
cur = db.cursor()

query = """
SELECT * FROM real_estate.home_data_summary LIMIT 10;
"""

print(query)
cur.execute(query)

result = cur.fetchall()
print(result)
# db.commit()
# print("records commited: {}").format(row)
db.close()