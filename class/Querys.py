from Store import *
import pandas as ps
from Visit import *
from Refrigerator import *
from Solidarity_Product import *
from Water import *
from Schedule import *
from Branding import *
from Info_Store import *

class Query:

	def __init__(self, connection, stores):
		self.connection = connection
		self.stores = stores

	def query_date(self, n_days):
		sheet1 = self.connection.get_sheet(1)
		sheet2 = self.connection.get_sheet(2)
		df1 = ps.DataFrame(sheet1.get_all_records())
		df2 = ps.DataFrame(sheet2.get_all_records())

		tiendas = {}
		for i in range(0,len(df2)):
			nombre_tienda = df2['Tienda'][i].split(' ')
			nombre_tienda_final = nombre_tienda[1]
			for j in range(2, len(nombre_tienda)):
				nombre_tienda_final += ' '+nombre_tienda[j]
			tiendas[nombre_tienda_final] = i
		stors = {}
		for value in tiendas:
			name = df2['Tienda'][tiendas[value]]
			manager = df2['Gerente'][tiendas[value]]
			cellphone = str(df2['Celular'][tiendas[value]])
			anexed = str(df2['Anexo Gte. Tda.'][tiendas[value]])
			phone = str(df2['Teléfono'][tiendas[value]])
			regional_manager = df2['Gte. Regional'][tiendas[value]]
			direction = df2['Dirección'][tiendas[value]]
			stors[value] = Info_Store(name, manager, cellphone, anexed, phone, regional_manager, direction)



		formato_fecha = "%m/%d/%Y %H:%M:%S"
		hoy = datetime.today()
		for index, rows in df1.iterrows():
			fecha = datetime.strptime(df1['Timestamp'][index],formato_fecha)
			
			if (hoy - fecha).days < n_days:
				tienda_actual = df1['Tienda visitada (agregado)'][index]

				clean = df1['El refrigerador, está limpio? '][index]
				working = df1['El refrigerador, funciona bien? '][index]
				visible = df1['El refrigerador, está visible?'][index]
				stock_refrigerator = df1['En relación al stock de aguas. Estaba lleno el refrigerador? '][index]
				concern_refrigerator = df1['En relación al stock de aguas. Alguien se preocupa de esto? '][index]
				quantity = df1['Cuantos refrigeradores tiene la tienda? '][index]
				if quantity == '':
					quantity = -1
				refrigerator = Refrigerator(clean,working,visible,stock_refrigerator,concern_refrigerator,quantity)
				
				has_branding = df1['El refrigerador, tiene branding TECHO?'][index]
				brand_looks_good = df1['Aspectos del Branding, se ve bien la marca? '][index]
				brand_is_clean = df1['Aspectos del Branding, está limpia la gráfica?'][index]
				brand_new = df1['Aspectos del Branding, se ve nuevo?'][index]
				brand = Branding(has_branding, brand_looks_good,brand_is_clean,brand_new)
				
				water = Water(refrigerator, brand)

				stock_sp = df1['En relación al stock de producto solidario. Había suficiente stock? '][index]
				concern_sp = df1['En relación al stock de producto solidario. Alguien se preocupa de esto? '][index]
				solidarity_product = Solidarity_Product(stock_sp, concern_sp)

				schedule_name = df1['¿Cual fue el horario de la visita?'][index]
				is_good = df1['¿Fue un buen horario de visita?'][index]
				schedule = Schedule(schedule_name,is_good)

				receivers = df1['¿Quién o quienes te recibió en la tienda? '][index]
				qualification = df1['Cómo calificas la visita? Del 1 al 10. '][index]
				comments = df1['Comentarios '][index]

				visit = Visit(fecha, receivers, qualification, comments,water,solidarity_product,schedule)				

				self.stores.add_store(tienda_actual)
				self.stores.get_store(tienda_actual).add_visit(visit)
				for value in stors:
					if value in tienda_actual:
						self.stores.get_store(tienda_actual).set_info(stors[value])