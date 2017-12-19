import pandas as ps
from datetime import datetime, date, time, timedelta
from Store import *
from Connection import *
from Store import *
from Querys import *
from List_Stores import *


connection = Connection("Visitas Sodimac (Responses)", 'client_secret.json')
sheet1 = connection.get_sheet1()

df = ps.DataFrame(sheet1.get_all_records())

stores = List_Stores()

querys = Query(df, stores)
querys.query_date(50)


my_dboard = dashboard.Dashboard()
my_dboard.get_preview()