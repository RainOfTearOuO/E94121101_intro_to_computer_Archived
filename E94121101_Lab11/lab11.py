# 客家委員會桐花景點步道(最後更新為110年5月，無網站，不再更新)
# https://data.gov.tw/dataset/166163

import pymysql.cursors
import requests
import json

# Get API Data
test = requests.get("https://cloud.hakka.gov.tw/Pub/Opendata/DTST20231000005.json")
r = json.loads(test.text)

#Connect to the Database
try:
    connection = pymysql.connect(host='192.168.137.38',
                                 user='E94121101',
                                 password='0000',
                                 database='wordpress',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("Connection Success")
except Exception as error: # if catch an error, print it out
    print(error)

with connection:
    with connection.cursor() as cursor:

        sql = "INSERT INTO `客家委員會桐花景點步道` (`SEQNO`,`viewpoint`,`address`,`LocalCallService`,`transportation_1`,`transportation_2`,`memo`,`charge`,`latitude`,`longitude`,`registration_time`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for i in range( len( r ) ):
            cursor.execute(sql, (r[i]['SEQNO'], r[i]['viewpoint'], r[i]['address'], r[i]['LocalCallService'], r[i]['transportation_1'], r[i]['transportation_2'], r[i]['memo'], r[i]['charge'], r[i]['latitude'], r[i]['longitude'], r[i]['registration_time']))

    connection.commit()
    cursor.close()