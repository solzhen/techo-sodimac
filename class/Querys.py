from Store import *
import pandas as ps
from Visit import *
from Refrigerator import *
from Solidarity_Product import *
from Water import *
from Schedule import *

class Query:

	def __init__(self, dataframe, stores):
		self.dataframe = dataframe
		self.stores = stores

	def query_date(self, n_days):
		formato_fecha = "%m/%d/%Y %H:%M:%S"
		hoy = datetime.today()
		for index, rows in self.dataframe.iterrows():
			fecha = datetime.strptime(self.dataframe['Timestamp'][index],formato_fecha)
			
			if (hoy - fecha).days < n_days:
				tienda_actual = self.dataframe['Tienda visitada (agregado)'][index]

				clean = self.dataframe['El refrigerador, está limpio? '][index]
				working = self.dataframe['El refrigerador, funciona bien? '][index]
				visible = self.dataframe['El refrigerador, está visible?'][index]
				stock_refrigerator = self.dataframe['En relación al stock de aguas. Estaba lleno el refrigerador? '][index]
				concern_refrigerator = self.dataframe['En relación al stock de aguas. Alguien se preocupa de esto? '][index]
				refrigerator = Refrigerator(clean,working,visible,stock_refrigerator,concern_refrigerator)
				water = Water(refrigerator)

				stock_sp = self.dataframe['En relación al stock de producto solidario. Había suficiente stock? '][index]
				concern_sp = self.dataframe['En relación al stock de producto solidario. Alguien se preocupa de esto? '][index]
				solidarity_product = Solidarity_Product(stock_sp, concern_sp)

				schedule_name = self.dataframe['¿Cual fue el horario de la visita?'][index]
				is_good = self.dataframe['¿Fue un buen horario de visita?'][index]
				schedule = Schedule(schedule_name,is_good)

				receivers = self.dataframe['¿Quién o quienes te recibió en la tienda? '][index]
				qualification = self.dataframe['Cómo calificas la visita? Del 1 al 10. '][index]
				comments = self.dataframe['Comentarios '][index]

				visit = Visit(fecha, receivers, qualification, comments,water,solidarity_product,schedule)				

				self.stores.add_store(tienda_actual)
				self.stores.get_store(tienda_actual).add_visit(visit)