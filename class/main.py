#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import pandas as ps
from datetime import datetime, date, time, timedelta
from Store import *
from Connection import *
from Store import *
from Querys import *
from List_Stores import *



class App():

	def __init__(self):
		self.stores = None

		self.root = Tk()
		self.root.geometry('800x900')
		self.root.title('Sodimac - Techo')

		self.days = Entry(self.root)
		self.days.pack(side=TOP)
		self.days.insert('1','30')

		self.days_button = Button(self.root, text = 'Dias a Consultar',
			command = self.consult)
		self.days_button.pack(side=TOP)

		self.text_info = Text(self.root)
		self.text_info.pack(fill = "both", expand = True)

		self.button_visited_stores = Button(self.root, text = 'Tiedas Visitadas',
			command = self.visited_stores)
		self.button_visited_stores.pack(side=LEFT)

		self.button_not_visited_stores = Button(self.root, text = 'Tiedas No Visitadas',
			command = self.not_visited_stores)
		self.button_not_visited_stores.pack(side=LEFT)

		self.button_refrigerators = Button(self.root, text = 'Refrigeradores',
			command = self.refrigerators)
		self.button_refrigerators.pack(side=LEFT)

		self.button_info_water = Button(self.root, text = 'Agua',
			command = self.info_water)
		self.button_info_water.pack(side=LEFT)

		self.button_info_sp = Button(self.root, text = 'Producto Solidario',
			command = self.info_sp)
		self.button_info_sp.pack(side=LEFT)


		
		self.root.mainloop()

	def consult(self):
		connection = Connection("Visitas Sodimac (Responses)", 'client_secret.json')
		sheet1 = connection.get_sheet1()

		df = ps.DataFrame(sheet1.get_all_records())

		self.stores = List_Stores()

		querys = Query(df, self.stores)
		days = int(self.days.get())
		querys.query_date(days)

		self.visited_stores()

	def visited_stores(self):
		self.text_info.delete("1.0", END)
		ans = "Total Tiendas Visitadas: "+str(self.stores.total_visited())+"\n\n"
		ans += "Tiendas Visitadas Zona Norte: \n"
		for value in self.stores.norte_visited:
			ans += value+"\n"
		ans += "\n"
		ans += "Tiedas visitadas Zona Centro:\n"
		for value in self.stores.centro_visited:
			ans += value +"\n"
		ans += "\n"
		ans += "Tiendas visitadas Region Metropolitana:\n"
		for value in self.stores.rm_visited:
			ans += value +"\n"
		ans += "\n"
		ans += "Tiendas visitadas Zona Sur:\n"
		for value in self.stores.sur_visited:
			ans += value +"\n"
		ans += "\n"


		self.text_info.insert("1.0",ans)

	def not_visited_stores(self):
		self.text_info.delete("1.0", END)
		ans = "Total Tiendas no Visitadas: "+str(self.stores.not_total_visited())+"\n\n"
		ans += "Tiendas no visitadas Zona Norte: \n"
		for value in self.stores.not_visited_norte():
			ans += value+"\n"
		ans += "\n"
		ans += "Tiedas no visitadas Zona Centro:\n"
		for value in self.stores.not_visited_centro():
			ans += value +"\n"
		ans += "\n"
		ans += "Tiendas no visitadas Region Metropolitana:\n"
		for value in self.stores.not_visited_rm():
			ans += value +"\n"
		ans += "\n"
		ans += "Tiendas no visitadas Zona Sur:\n"
		for value in self.stores.not_visited_sur():
			ans += value +"\n"
		ans += "\n"


		self.text_info.insert("1.0",ans)

	def refrigerators(self):
		self.text_info.delete("1.0", END)
		ans = "Refrigeradores sucios: \n"
		ans += "\n"
		ans += "Zona Norte:\n"
		for value in self.stores.norte_visited:
			cant = len(self.stores.norte_visited[value].visits_refrigerator_not_clean())
			if cant > 0:
				ans += value +"\n"
				ans += "	Sucio "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Centro:\n"
		for value in self.stores.centro_visited:
			cant = len(self.stores.centro_visited[value].visits_refrigerator_not_clean())
			if cant > 0:
				ans += value +"\n"
				ans += "	Sucio "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Region Metropolitana:\n"
		for value in self.stores.rm_visited:
			cant = len(self.stores.rm_visited[value].visits_refrigerator_not_clean())
			if cant > 0:
				ans += value +"\n"
				ans += "	Sucio "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Sur:\n"
		for value in self.stores.sur_visited:
			cant = len(self.stores.sur_visited[value].visits_refrigerator_not_clean())
			if cant > 0:
				ans += value +"\n"
				ans += "	Sucio "+str(cant)+ " veces\n"
		ans += "\n"
		ans += "\n"


		ans += "Refrigeradores No utiles\n"
		ans += "\n"
		ans += "Zona Norte:\n"
		for value in self.stores.norte_visited:
			cant = len(self.stores.norte_visited[value].visits_refrigerator_not_working())
			if cant > 0:
				ans += value +"\n"
				ans += "	No util "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Centro:\n"
		for value in self.stores.centro_visited:
			cant = len(self.stores.centro_visited[value].visits_refrigerator_not_working())
			if cant > 0:
				ans += value +"\n"
				ans += "	No util "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Region Metropolitana:\n"
		for value in self.stores.rm_visited:
			cant = len(self.stores.rm_visited[value].visits_refrigerator_not_working())
			if cant > 0:
				ans += value +"\n"
				ans += "	No util "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Sur:\n"
		for value in self.stores.sur_visited:
			cant = len(self.stores.sur_visited[value].visits_refrigerator_not_working())
			if cant > 0:
				ans += value +"\n"
				ans += "	No util "+str(cant)+ " veces\n"
		ans += "\n"
		ans += "\n"

		ans += "Refrigeradores No visibles\n"
		ans += "\n"
		ans += "Zona Norte:\n"
		for value in self.stores.norte_visited:
			cant = len(self.stores.norte_visited[value].visits_refrigerator_not_visible())
			if cant > 0:
				ans += value +"\n"
				ans += "	No visible "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Centro:\n"
		for value in self.stores.centro_visited:
			cant = len(self.stores.centro_visited[value].visits_refrigerator_not_visible())
			if cant > 0:
				ans += value +"\n"
				ans += "	No visible "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Region Metropolitana:\n"
		for value in self.stores.rm_visited:
			cant = len(self.stores.rm_visited[value].visits_refrigerator_not_visible())
			if cant > 0:
				ans += value +"\n"
				ans += "	No visible "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Sur:\n"
		for value in self.stores.sur_visited:
			cant = len(self.stores.sur_visited[value].visits_refrigerator_not_visible())
			if cant > 0:
				ans += value +"\n"
				ans += "	No visible "+str(cant)+ " veces\n"
		ans += "\n"

		self.text_info.insert("1.0",ans)

	def info_water(self):
		self.text_info.delete("1.0", END)
		ans = "Tiendas sin suficiente stock de agua: \n"
		ans += "\n"
		ans += "Zona Norte:\n"
		for value in self.stores.norte_visited:
			cant = len(self.stores.norte_visited[value].visit_water_not_has_stock())
			if cant > 0:
				ans += value +"\n"
				ans += "	Poco stock "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Centro:\n"
		for value in self.stores.centro_visited:
			cant = len(self.stores.centro_visited[value].visit_water_not_has_stock())
			if cant > 0:
				ans += value +"\n"
				ans += "	Poco stock "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Region Metropolitana:\n"
		for value in self.stores.rm_visited:
			cant = len(self.stores.rm_visited[value].visit_water_not_has_stock())
			if cant > 0:
				ans += value +"\n"
				ans += "	Poco stock "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Sur:\n"
		for value in self.stores.sur_visited:
			cant = len(self.stores.sur_visited[value].visit_water_not_has_stock())
			if cant > 0:
				ans += value +"\n"
				ans += "	Poco stock "+str(cant)+ " veces\n"
		ans += "\n\n"


		ans += "Tiendas sin encargado de agua: \n"
		ans += "\n"
		ans += "Zona Norte:\n"
		for value in self.stores.norte_visited:
			cant = len(self.stores.norte_visited[value].visit_water_not_has_concern())
			if cant > 0:
				ans += value +"\n"
				ans += "	Sin encargado "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Centro:\n"
		for value in self.stores.centro_visited:
			cant = len(self.stores.centro_visited[value].visit_water_not_has_concern())
			if cant > 0:
				ans += value +"\n"
				ans += "	Sin encargado "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Region Metropolitana:\n"
		for value in self.stores.rm_visited:
			cant = len(self.stores.rm_visited[value].visit_water_not_has_concern())
			if cant > 0:
				ans += value +"\n"
				ans += "	Sin encargado "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Sur:\n"
		for value in self.stores.sur_visited:
			cant = len(self.stores.sur_visited[value].visit_water_not_has_concern())
			if cant > 0:
				ans += value +"\n"
				ans += "	Sin encargado "+str(cant)+ " veces\n"
		ans += "\n"

		self.text_info.insert("1.0",ans)


	def info_sp(self):
		self.text_info.delete("1.0", END)
		ans = "Tiendas sin suficiente stock de producto solidario: \n"
		ans += "\n"
		ans += "Zona Norte:\n"
		for value in self.stores.norte_visited:
			cant = len(self.stores.norte_visited[value].visit_sp_not_has_stock())
			if cant > 0:
				ans += value +"\n"
				ans += "	Poco stock "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Centro:\n"
		for value in self.stores.centro_visited:
			cant = len(self.stores.centro_visited[value].visit_sp_not_has_stock())
			if cant > 0:
				ans += value +"\n"
				ans += "	Poco stock "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Region Metropolitana:\n"
		for value in self.stores.rm_visited:
			cant = len(self.stores.rm_visited[value].visit_sp_not_has_stock())
			if cant > 0:
				ans += value +"\n"
				ans += "	Poco stock "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Sur:\n"
		for value in self.stores.sur_visited:
			cant = len(self.stores.sur_visited[value].visit_sp_not_has_stock())
			if cant > 0:
				ans += value +"\n"
				ans += "	Poco stock "+str(cant)+ " veces\n"
		ans += "\n\n"


		ans += "Tiendas sin encargado de producto solidario: \n"
		ans += "\n"
		ans += "Zona Norte:\n"
		for value in self.stores.norte_visited:
			cant = len(self.stores.norte_visited[value].visit_sp_not_has_concern())
			if cant > 0:
				ans += value +"\n"
				ans += "	Sin encargado "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Centro:\n"
		for value in self.stores.centro_visited:
			cant = len(self.stores.centro_visited[value].visit_sp_not_has_concern())
			if cant > 0:
				ans += value +"\n"
				ans += "	Sin encargado "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Region Metropolitana:\n"
		for value in self.stores.rm_visited:
			cant = len(self.stores.rm_visited[value].visit_sp_not_has_concern())
			if cant > 0:
				ans += value +"\n"
				ans += "	Sin encargado "+str(cant)+ " veces\n"
		ans += "\n"

		ans += "Zona Sur:\n"
		for value in self.stores.sur_visited:
			cant = len(self.stores.sur_visited[value].visit_sp_not_has_concern())
			if cant > 0:
				ans += value +"\n"
				ans += "	Sin encargado "+str(cant)+ " veces\n"
		ans += "\n"

		self.text_info.insert("1.0",ans)



def main():
	my_app = App()

if __name__ == '__main__':
	main()