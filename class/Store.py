from datetime import datetime, date, time, timedelta
from Visit import *

class Store:

	def __init__(self, name):
		self.name = name
		self.visits = {}
		self.las_visit = None

	def add_visit(self, new_visit):
		self.visits[new_visit.date] = new_visit
		self.last_visit = new_visit

	def count_visits(self,init,final):
		ans = 0
		for key in self.visits:
			if visits[key].date_is_in_range(init,final):
				ans +=1
		return ans

	def count_receivers(self):
		list_receivers = {'Jefe de tienda':0, 'Asistente Social':0,
		'Jefe de Cajas':0, 'Encargado de RRHH':0, 'Jefe de voluntariado':0}
		
		for key in self.visits:
			for value in self.visits[key].receivers:
				list_receivers[value] +=1

		return list_receivers

	def visits_refrigerator_not_clean(self):
		ans = []
		for key in self.visits:
			if not self.visits[key].refrigerator_is_clean():
				ans.append(self.visits[key])
		return ans

	def visits_refrigerator_not_working(self):
		ans = []
		for key in self.visits:
			if not self.visits[key].refrigerator_is_working():
				ans.append(self.visits[key])
		return ans

	def visits_refrigerator_not_visible(self):
		ans = []
		for key in self.visits:
			if not self.visits[key].refrigerator_is_visible():
				ans.append(self.visits[key])
		return ans

	def visit_water_not_has_stock(self):
		ans = []
		for key in self.visits:
			if not self.visits[key].water_has_stock():
				ans.append(self.visits[key])
		return ans

	def visit_water_not_has_concern(self):
		ans = []
		for key in self.visits:
			if not self.visits[key].water_has_concern():
				ans.append(self.visits[key])
		return ans

	def visit_sp_not_has_stock(self):
		ans = []
		for key in self.visits:
			if not self.visits[key].sp_has_stock():
				ans.append(self.visits[key])
		return ans

	def visit_sp_not_has_concern(self):
		ans = []
		for key in self.visits:
			if not self.visits[key].sp_has_concern():
				ans.append(self.visits[key])
		return ans

	def avg_qualification(self):
		ans = 0
		for key in self.visits:
			ans += self.visits[key].qualification
		return ans/len(self.visits)

	