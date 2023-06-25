import mysql.connector
from json import loads, dumps
from flask import jsonify
import pandas
from decimal import Decimal




def methode():
    year = 2016
    month = "August"
    day = 16
    dbverbinding = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
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

def methode2():
    print("hoi")
    df = pandas.read_csv("Pokemon.csv")
    result = df.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4)  
    
print(methode2())