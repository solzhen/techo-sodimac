
class Schedule:

	def __init__(self, schedule, good):
		options = {'Sí':1, 'No':0}

		self.schedule = schedule
		self.good = options[good]

	def is_good(self):
		return self.good


hola = Schedule('hola', 'No')
print(hola.is_good())