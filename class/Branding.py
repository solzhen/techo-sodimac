
class Branding:


	def __init__(self, brand, clean, new):
		options = {'Sí':1, 'No':0}
		
		self.look_good = options[brand]
		self.clean = options[clean]
		self.new = options[new]

	def looks_good(self):
		return self.look_good == 1

	def is_clean(self):
		return self.clean == 1

	def is_new(self):
		return self.new == 1