
class Branding:


	def __init__(self, has_branding, brand, clean, new):
		options = {'Sí':1, 'No':0}
		
		self.has_branding = options[has_branding]
		self.look_good = options[brand]
		self.clean = options[clean]
		self.new = options[new]

	def looks_good(self):
		return self.look_good == 1

	def is_clean(self):
		return self.clean == 1

	def is_new(self):
		return self.new == 1

	def hasnt_branding(self):
		return self.has_branding == 0