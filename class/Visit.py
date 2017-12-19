
class Visit:

	def __init__(self, date, receivers, qualification, comments):
		self.date = date
		self.receivers = split_receivers(receivers)
		self.qualification = qualification
		self.comments = comments
		self.waters
		self.solidarity_product
		self.schedule

	def split_receiver(receivers):
		return receivers.split(', ')

	def set_branding(self, branding):
		self.branding = branding

	def set_schedule(self, schedule):
		self.schedule = schedule