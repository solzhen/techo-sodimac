class Refrigerator:

	def __init__(self, clean, working, visible, quantity, stock, concern):
		options = {'Sí':1, 'No':0}

		self.clean = options[clean]
		self.working = options[working]
		self.visible = options[visible]
		self.quantity = quantity
		self.stock = option[stock]
		self.concern = option[concern]

	def is_clean(self):
		return self.clean

	def is_working(self):
		return self.working

	def is_visible(self):
		return self.visible

	def get_quantity(self):
		return self.quantity

	def have_concern(self):
		return self.concern

	def is_stock(self):
		return self.stock

