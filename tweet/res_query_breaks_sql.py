import mysql.connector
import sys, base64
from twython import Twython
from auth import *
from datetime import date, timedelta

today = date.today()
first_day = today.replace(day=1)
last_month = first_day - timedelta(days=1)
month_date = last_month.strftime("%b-%Y")

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#configs for database

db = mysql.connector.connect(
  host=host,
  user=user,
  passwd=grantPass,
  db="real_estate"
)
print('Connected to database \n')
cur = db.cursor()

def message():
  up_chart = b'\xF0\x9F\x93\x88'
  down_chart = b'\xF0\x9F\x93\x89'
  even = b'\xE2\x86\x94'
  message_list = []
  for res in responses:
    if '-' in str(res[1]):
      new_res = (*res, '', down_chart)
      message_list.append(new_res)
    elif str(res[1]) == '0.0':
      new_res = (*res, '', even)
      message_list.append(new_res)
    else:
      new_res = (*res,  '+', up_chart)
      message_list.append(new_res)
  return message_list

table_list = ['res','res_condo', 'condo']
for table in table_list:
  update_query= """
  select r.region_name 
  , ROUND(h.precent_chg_median_price, 1)
  from {0}_home_data_summary h
  inner join dim_regions r on h.region_id = r.region_id
  where 1=1
  and month_year = '{1}'
  """.format(table, month_date)

  cur.execute(update_query)
  responses = cur.fetchall()
  print(responses)
  # if table == 'res':
  #   tweet_table = 'Residential SFH'
  # elif table == 'condo':
  #   tweet_table = 'Condo'
  # else:
  #   tweet_table = 'Res+Condo'

  # top_part = "OCT 2019 \nYoY Median {} Prices:".format(tweet_table)
  # bottom_part = '#Seattle #seattlerealestate #realestate'
  # w_seattle = "{0} {1}{2}% {3}".format(message()[0][3].decode(), message()[0][2], message()[0][1],message()[0][0])
  # se_seattle = "{0} {1}{2}% {3}".format(message()[1][3].decode(), message()[1][2], message()[1][1],message()[1][0])
  # sw_seattle = "{0} {1}{2}% {3}".format(message()[2][3].decode(), message()[2][2], message()[2][1],message()[2][0])
  # cap_seattle = "{0} {1}{2}% {3}".format(message()[3][3].decode(), message()[3][2], message()[3][1],message()[3][0])
  # queen_anne = "{0} {1}{2}% {3}".format(message()[4][3].decode(), message()[4][2], message()[4][1],message()[4][0])
  # ballard = "{0} {1}{2}% {3}".format(message()[5][3].decode(), message()[5][2], message()[5][1],message()[5][0])
  
  # formatted_message = ("{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}".format(top_part
  #                                                           ,w_seattle
  #                                                           ,se_seattle
  #                                                           ,sw_seattle
  #                                                           ,cap_seattle
  #                                                           ,queen_anne
  #                                                           ,ballard
  #                                                           ,bottom_part))
  # print(formatted_message)

  # twitter.update_status(status=formatted_message)
  # print("Tweeted: %s" % formatted_message)



db.close()