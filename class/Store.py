from datetime import datetime, date, time, timedelta

class Store:

	def __init__(self, name):
		self.name = name
		self.visits = {}

	def add_visit(self, new_visit):
		visit[new_visit.date] = new_visit
