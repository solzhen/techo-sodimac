
class Schedule:

	options = {'Sí':1, 'No':0}

	def __init__(self, schedule, good):
		self.schedule = schedule
		self.good = options[good]

	def is_good(self):
		return self.good