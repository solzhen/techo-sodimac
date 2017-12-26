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

	def has_refrigerator(self):
		return self.waters.refrigerator.has_refrigerator()

	def quantity_refrigerator(self):
		return self.waters.refrigerator.quantity

	def water_has_stock(self):
		return self.waters.refrigerator.has_stock()

	def water_has_concern(self):
		return self.waters.refrigerator.has_concern()

	def branding_looks_good(self):
		return self.waters.branding.looks_good()

	def branding_is_clean(self):
		return self.waters.branding.is_clean()

	def branding_is_new(self):
		return self.waters.branding.is_new()

	def sp_has_stock(self):
		return self.solidarity_product.has_stock()

	def sp_has_concern(self):
		return self.solidarity_product.has_concern()


