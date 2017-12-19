from Store import *
# -*- coding: utf-8 -*-

class List_Stores:

	def __init__(self):
		self.norte_visited = {}
		self.centro_visited = {}
		self.sur_visited = {}
		self.rm_visited = {}

		self.stores_norte = {"NORTE-  Hc Antofagasta- Balmaceda Nº 2355, Interior Recinto Portuario Extremo Sur, dentro del Mall, Antofagasta":0,
		"NORTE- Hc Iquique Héroes de la Concepción Nº 2311, Iquique":0,
		"NORTE- Hc Calama Balmaceda Nº 3398, Calama":0,
		"NORTE 4 Hc Arica Av. Santa María Nº 2985, Arica":0,
		"NORTE Co Antofagasta- Av. Antonio Rendic Nº 6852, Antofagasta":0,
	    "NORTE HC Alto Hospicio- Av. Los Aromos Nº 2780, Alto Hospicio":0,
	    "NORTE Hc Copiapó Cordillera- Av. Los Carrera 4723, Copiapó":0}

		self.stores_centro = {"CENTRO- Co Viña del Mar Limache Nº 3119, Viña del Mar":0,
	    "CENTRO- Hc Viña del Mar 15 Norte Nº 961, Viña del Mar":0,
	    "CENTRO- Co Rancagua Koke Nº 011, Rancagua":0,
	    "CENTRO- Co Valparaíso Yungay Nº 2516, Valparaíso":0,
	    "CENTRO- Hc La Serena Av. Fco. de Aguirre Nº 02, La Serena":0,
	    "CENTRO- Hc Rancagua Av. Albert Einstein Nº 297, Rancagua":0,
	    "CENTRO- Hc El Belloto Avenida Freire Nº 1351, Quilpué":0,
	    "CENTRO- Hc Reñaca Alessandri Nº 4085, Reñaca Alto, Viña del Mar":0,
	    "CENTRO- Hc Coquimbo- Ruta 5 Norte Nº 849, Coquimbo":0,
	    "CENTRO- Hc Quinta Vergara Av. Valparaíso Nº 1070, Viña del Mar":0}

		self.stores_sur = {"SUR- Hc Concepción Los Carrera Nº 1175, Concepción":0,
	    "SUR- Hc Osorno René Soriano Nº 2619, Osorno":0,
	    "SUR- Hc Los Angeles Av. Alemania Nº 850, Los Angeles":0,
	    "SUR- Hc Valdivia Av. Picarte Nº 3349, Valdivia":0,
	    "SUR- Hc Puerto Montt Av. Presidente Ibañez Nº 650, Puerto Montt":0,
	    "SUR- Hc Temuco Cautín Caupolicán Nº 0457, Temuco":0,
	    "SUR- Hc Mall Plaza El Trébol Av. Pdte. Jorge Alessandri Nº 3177, Concepción":0,
	    "SUR- Hc Autopista Talcahuano Autopista Concep-Talcahuano Nº 9200, comuna Hualpén, Talcahuano":0,
	    "SUR- Hc Mall Bío Bío Av. Los Carreras Poniente Nº 301, Concepción":0}

		self.stores_rm = {"RM- Hc San Miguel Gran Avda. José Miguel Carrera Nº 5508, San Miguel, Santiago":0,
	    "RM- Co Cantagallo Av. Las Condes Nº 12422, Lo Barnechea, Santiago":0,
	    "RM- HC San Bernardo Jorge Alessandri Rodríguez N°20.040, Local TH – 100Y PC100, San Bernardo":0,
	    "RM- Co Ñuñoa Vicuña Mackenna Nº 680, Ñuñoa, Santiago":0,
	    "RM- Hc Las Condes Av. Las Condes Nº 11049, Las Condes, Santiago":0,
	    "RM- Co Maipú Av. Pajaritos Nº 2418, Maipú, Santiago":0,
	    "RM- Hc Nueva La Florida Av.José Pedro Alessandri Nº 6402, La Florida, Santiago":0,
	    "RM- Hc Huechuraba Av. Américo Vespucio Nº 1737, Huechuraba, Santiago":0,
	    "RM- Co La Florida Av. Vicuña Mackenna Nº 9101, La Florida, Santiago":0,
	    "RM- Hc Ñuble Av. Vicuña Mackenna Nº 1700, Ñuñoa, Santiago":0,
	    "RM- Hc La Reina Av. Pdte. Jorge Alessandri Nº 1347, La Reina, Santiago":0,
	    "RM- HC El Bosque Gran Avda. José Miguel Carrera Nº 10375, El Bosque, Santiago":0,
	    "RM- Hc Puente Alto Av. Concha y Toro Nº 1315, Puente Alto, Santiago":0,
	    "RM- Co Huechuraba Pedro Fontova Nº 5810, Huechuraba, Santiago":0,
	    "RM. Hc Maipú Av. Pajaritos Nº 4444, Maipú, Santiago":0,
	    "RM.- Hc Plaza Vespucio Américo Vespucio Nº 7310, La Florida, Santiago":0,
	    "RM- Hc Cerrillos Américo Vespucio Nº 1501, Cerrillos, Santiago":0,
	    "RM- Hc Quilicura Av. Manuel A. Matta Nº 581, Quilicura":0,
	    "RM- Hc Tobalaba Av. Camilo Henríquez Nº 3692, Puente Alto, Santiago":0}


	def add_store(self, name):
		if name.startswith('NOR'):
			if self.stores_norte[name] == 0:
				self.stores_norte[name] += 1
				self.norte_visited[name] = Store(name)
			else:
				self.stores_norte[name] += 1

		elif name.startswith('SUR'):
			if self.stores_sur[name] == 0:
				self.stores_sur[name] += 1
				self.sur_visited[name] = Store(name)
			else:
				self.stores_sur[name] += 1

		elif name.startswith('CEN'):
			if self.stores_centro[name] == 0:
				self.stores_centro[name] += 1
				self.centro_visited[name] = Store(name)
			else:
				self.stores_centro[name] += 1

		else:
			if self.stores_rm[name] == 0:
				self.stores_rm[name] += 1
				self.rm_visited[name] = Store(name)
			else:
				self.stores_rm[name] +=1

	def get_store(self,name):
		if name.startswith('NOR'):
			if self.stores_norte[name] == 0:
				return None
			else:
				return self.norte_visited[name]
		elif name.startswith('SUR'):
			if self.stores_sur[name] == 0:
				return None
			else:
				return self.sur_visited[name]
		elif name.startswith('CEN'):
			if self.stores_centro[name] == 0:
				return None
			else:
				return self.centro_visited[name]
		else:
			if self.stores_rm[name] == 0:
				return None
			else:
				return self.rm_visited[name]


	def cant_norte_visited(self):
		return len(self.norte_visited)

	def cant_centro_visited(self):
		return len(self.centro_visited)

	def cant_sur_visited(self):
		return len(self.sur_visited)

	def cant_rm_visited(self):
		return len(self.rm_visited)

	def total_visited(self):
		return self.cant_rm_visited() + self.cant_sur_visited()+ self.cant_centro_visited() + self.cant_norte_visited()

	def not_visited_rm(self):
		ans = []
		for key in self.stores_rm:
			if self.stores_rm[key] == 0:
				ans.append(key)
		return ans

	def not_visited_norte(self):
		ans = []
		for key in self.stores_norte:
			if self.stores_norte[key] == 0:
				ans.append(key)
		return ans

	def not_visited_centro(self):
		ans = []
		for key in self.stores_centro:
			if self.stores_centro[key] == 0:
				ans.append(key)
		return ans

	def not_visited_sur(self):
		ans = []
		for key in self.stores_sur:
			if self.stores_sur[key] == 0:
				ans.append(key)
		return ans

	def not_total_visited(self):
		return len(self.not_visited_rm())+ len(self.not_visited_norte())+ len(self.not_visited_centro()) + len(self.not_visited_sur())
