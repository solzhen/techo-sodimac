
class Branding:


	def __init__(self, brand, clean, new):
		options = {'Sí':1, 'No':0}
		
		self.brand = options[brand]
		self.clean = options[clean]
		self.new = options[new]

	def looks_good(self):
		return self.brand

	def is_clean(self):
		return self.clean

	def is_new(self):
		return self.new