import mysql.connector
import windowsgebruik
import json
from flask import jsonify

from decimal import Decimal

#Does quasi the same things as json.loads from here: https://pypi.org/project/dynamodb-json/
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

def methode():
    year = 2016
    month = "August"
    day = 16
    dbverbinding = mysql.connector.connect(
        host='localhost',
        port=windowsgebruik.krijgpoort(),
        user='root',
        password=windowsgebruik.krijgwachtwoord(),
        database='hotel_booking'
    )
    mijncursor = dbverbinding.cursor()
    sql_check_data = 'SELECT * FROM hotel_booking WHERE arrival_date_year = %s AND arrival_date_month = %s AND arrival_date_day_of_month = %s'
    mijncursor.execute(sql_check_data, (year, month, day)) # execute(SQL statement, (hier de waarden voor de plekken %s en op volgorde)
    mydata = mijncursor.fetchall()

    keys = [i[0] for i in mijncursor.description]

    data = [
        dict(zip(keys, row)) for row in mydata
    ]
    return data

#print(methode())