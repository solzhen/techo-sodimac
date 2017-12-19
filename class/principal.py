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
querys.query_date(40)

print("norte: "+str(stores.cant_norte_visited()))
print("centro: "+str(stores.cant_centro_visited()))
print("sur: "+str(stores.cant_sur_visited()))
print("rm: "+str(stores.cant_rm_visited()))

for key in stores.sur_visited:
	print(key)
