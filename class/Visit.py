from Water import *
from Solidarity_Product import *
from Schedule import *

class Visit:

	
	def __init__(self, date, receivers, qualification, comments,waters,solidarity_product,schedule):
		self.date = date
		self.receivers = receivers.split(', ')
		self.qualification = int(qualification)
		self.comments = comments
		self.waters = waters
		self.solidarity_product = solidarity_product
		self.schedule = schedule

	def date_is_in_range(self, init, final):
		return self.date >= init and self.date <= final

	def refrigerator_is_clean(self):
		return self.waters.refrigerator.is_clean()

	def refrigerator_is_working(self):
		return self.waters.refrigerator.is_working()

	def refrigerator_is_visible(self):
		return self.waters.refrigerator.is_visible()

	def water_has_stock(self):
		return self.waters.refrigerator.has_stock()

	def water_has_concern(self):
		return self.waters.refrigerator.has_concern()

	def sp_has_stock(self):
		return self.solidarity_product.has_stock()

	def sp_has_concern(self):
		return self.solidarity_product.has_concern()
