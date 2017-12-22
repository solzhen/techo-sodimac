class Refrigerator:

	def __init__(self, clean, working, visible, stock, concern):
		options = {'Sí':1, 'No':0}

		self.clean = options[clean]
		self.working = options[working]
		self.visible = options[visible]
		self.stock = options[stock]
		self.concern = options[concern]

	def is_clean(self):
		return self.clean == 1

	def is_working(self):
		return self.working == 1

	def is_visible(self):
		return self.visible == 1

	def has_concern(self):
		return self.concern == 1

	def has_stock(self):
		return self.stock == 1

