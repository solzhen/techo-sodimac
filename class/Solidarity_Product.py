
class Solidarity_Product:

	def __init__(self, stock, concern):
		options = {'Sí':1, 'No':0}
		
		self.stock = options[stock]
		self.concern = options[concern]
		self.branding = None

	def has_stock(self):
		return self.stock == 1

	def has_concern(self):
		return self.concern == 1
