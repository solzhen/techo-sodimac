
class Social_Product:

	def __init__(self, stock, concern, branding):
		options = {'Sí':1, 'No':0}
		
		self.stock = options[stock]
		self.concern = concern[concern]
		self.branding = branding

	def is_stock(self):
		return self.stock

	def have_concern(self):
		return self.concern
