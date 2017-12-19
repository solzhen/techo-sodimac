from Store import *
import pandas as ps


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
				self.stores.add_store(tienda_actual)