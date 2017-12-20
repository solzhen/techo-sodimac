
class Schedule:

	def __init__(self, schedule, good):
		options = {'Sí':1, 'No':0}

		self.name = schedule
		self.good = options[good]

	def is_good(self):
		return self.good == 1