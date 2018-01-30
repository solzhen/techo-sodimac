from Store import *
from List_Stores import *

class Tables:

	def __init__(self):
		pass 

	def parse_link(self,link):
		return link.replace(' ','$')

	def reverse_parse_link(self,link):
		return link.replace('$',' ')


	def visited_stores(self, stores):
		ans = "<table>"
		ans += '<tr><th colspan="3">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Promedio Calificación</th><th>Visitas</th></tr>'
		for value in stores.norte_visited:
			ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
			ans += "<td>"+str(stores.norte_visited[value].avg_qualification())+"</td>"
			ans += "<td>"+str(stores.norte_visited[value].cant_visits())+"</td></tr>"
		ans += '</table><br>'

		ans += '<table>'
		ans += '<tr><th colspan="3">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Promedio Calificación</th><th>Visitas</th></tr>'
		for value in stores.centro_visited:
			ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
			ans += "<td>"+str(stores.centro_visited[value].avg_qualification())+"</td>"
			ans += "<td>"+str(stores.centro_visited[value].cant_visits())+"</td></tr>"
		ans += '</table><br>'

		ans += '<table>'
		ans += '<tr><th colspan="3">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Promedio Calificación</th><th>Visitas</th></tr>'
		for value in stores.rm_visited:
			ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
			ans += "<td>"+str(stores.rm_visited[value].avg_qualification())+"</td>"
			ans += "<td>"+str(stores.rm_visited[value].cant_visits())+"</td></tr>"
		ans += '</table><br>'

		ans += '<table>'
		ans += '<tr><th colspan="3">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Promedio Calificación</th><th>Visitas</th></tr>'
		for value in stores.sur_visited:
			ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
			ans += "<td>"+str(stores.sur_visited[value].avg_qualification())+"</td>"
			ans += "<td>"+str(stores.sur_visited[value].cant_visits())+"</td></tr>"
		ans +="</table>"

		return ans

	def not_visited_stores(self, stores):
		ans = "<table>"
		ans += '<tr><th>Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th></tr>'
		for value in stores.not_visited_norte():
			ans += "<tr><td>"+value+"</td>"
		ans += '</table><br>'

		ans += '<table>'
		ans += '<tr><th colspan="3">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th></tr>'
		for value in stores.not_visited_centro():
			ans += "<tr><td>"+value+"</td>"
		ans += '</table><br>'

		ans += '<table>'
		ans += '<tr><th colspan="3">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th></tr>'
		for value in stores.not_visited_rm():
			ans += "<tr><td>"+value+"</td>"
		ans += '</table><br>'

		ans += '<table>'
		ans += '<tr><th>Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th></tr>'
		for value in stores.not_visited_sur():
			ans += "<tr><td>"+value+"</td>"
		ans +="</table>"

		return ans

	def refrigerators_not_clean(self, stores):
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			cant = len(stores.get_store(value).visits_refrigerator_not_clean())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.centro_visited:
			cant = len(stores.get_store(value).visits_refrigerator_not_clean())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visits_refrigerator_not_clean())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visits_refrigerator_not_clean())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"
		return ans

	def refrigerators_not_working(self, stores):
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			cant = len(stores.get_store(value).visits_refrigerator_not_working())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.centro_visited:
			cant = len(stores.get_store(value).visits_refrigerator_not_working())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visits_refrigerator_not_working())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visits_refrigerator_not_working())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"
		return ans

	def refrigerators_not_visible(self, stores):
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			cant = len(stores.get_store(value).visits_refrigerator_not_visible())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.centro_visited:
			cant = len(stores.get_store(value).visits_refrigerator_not_visible())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visits_refrigerator_not_visible())
			if cant > 0:
				ans += "<tr><td>"+value+"</td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visits_refrigerator_not_visible())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"
		return ans

	def stores_without_refrigerator(self,stores):
		formato = "%d / %m / %Y"
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Fecha visita</th></tr>'
		for value in stores.norte_visited:
			visits = stores.get_store(value).visits_without_refrigerator()
			cant = len(visits)
			if cant > 0:
				ans += "<tr><td rowspan='"+str(cant)+"' ><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
				ans += "<td>"
				for visit in visits:
					ans += "<tr>"+visit.date.strftime(formato)+"</tr>"
			ans += "</td>"
			ans += "</tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			visits = stores.get_store(value).visits_without_refrigerator()
			cant = len(visits)
			if cant > 0:
				ans += "<tr><td rowspan='"+str(cant)+"' ><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
				ans += "<td>"
				for visit in visits:
					ans += "<tr>"+visit.date.strftime(formato)+"</tr>"
			ans += "</td>"
			ans += "</tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Fecha visita</th></tr>'
		for value in stores.norte_visited:
			visits = stores.get_store(value).visits_without_refrigerator()
			cant = len(visits)
			if cant > 0:
				ans += "<tr><td rowspan='"+str(cant)+"' ><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
				ans += "<td>"
				for visit in visits:
					ans += "<tr>"+visit.date.strftime(formato)+"</tr>"
			ans += "</td>"
			ans += "</tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Fecha visita</th></tr>'
		for value in stores.norte_visited:
			visits = stores.get_store(value).visits_without_refrigerator()
			cant = len(visits)
			if cant > 0:
				ans += "<tr><td rowspan='"+str(cant)+"' ><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
				ans += "<td>"
				for visit in visits:
					ans += "<tr>"+visit.date.strftime(formato)+"</tr>"
			ans += "</td>"
			ans += "</tr>"
		ans += "</table><br>"
		return ans


	def water_has_not_stock(self,stores):
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			cant = len(stores.get_store(value).visit_water_not_has_stock())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.centro_visited:
			cant = len(stores.get_store(value).visit_water_not_has_stock())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_water_not_has_stock())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_water_not_has_stock())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"
		return ans

	def water_has_not_concern(self,stores):
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			cant = len(stores.get_store(value).visit_water_not_has_concern())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.centro_visited:
			cant = len(stores.get_store(value).visit_water_not_has_concern())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_water_not_has_concern())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_water_not_has_concern())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"
		return ans

	def hasnt_branding(self,stores):
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			cant = len(stores.get_store(value).visit_hasnt_branding())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.centro_visited:
			cant = len(stores.get_store(value).visit_hasnt_branding())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_hasnt_branding())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_hasnt_branding())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"
		return ans

	def branding_not_looks_good(self,stores):
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			cant = len(stores.get_store(value).visit_branding_not_looks_good())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.centro_visited:
			cant = len(stores.get_store(value).visit_branding_not_looks_good())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_branding_not_looks_good())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_branding_not_looks_good())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"
		return ans

	def branding_not_is_clean(self,stores):
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			cant = len(stores.get_store(value).visit_branding_not_is_clean())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.centro_visited:
			cant = len(stores.get_store(value).visit_branding_not_is_clean())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_branding_not_is_clean())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_branding_not_is_clean())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"
		return ans

	def branding_not_is_clean(self,stores):
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			cant = len(stores.get_store(value).visit_branding_not_is_clean())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.centro_visited:
			cant = len(stores.get_store(value).visit_branding_not_is_clean())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_branding_not_is_clean())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_branding_not_is_clean())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"
		return ans

	def branding_not_is_new(self,stores):
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			cant = len(stores.get_store(value).visit_branding_not_is_new())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.centro_visited:
			cant = len(stores.get_store(value).visit_branding_not_is_new())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_branding_not_is_new())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_branding_not_is_new())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"
		return ans

	def ps_has_not_stock(self,stores):
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			cant = len(stores.get_store(value).visit_sp_not_has_stock())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.centro_visited:
			cant = len(stores.get_store(value).visit_sp_not_has_stock())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_sp_not_has_stock())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_sp_not_has_stock())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"
		return ans

	def ps_has_not_concern(self,stores):
		ans = "<table>"
		ans += '<tr><th colspan="2">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.norte_visited:
			cant = len(stores.get_store(value).visit_sp_not_has_concern())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.centro_visited:
			cant = len(stores.get_store(value).visit_sp_not_has_concern())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_sp_not_has_concern())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += '<tr><th colspan="2">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Veces</th></tr>'
		for value in stores.rm_visited:
			cant = len(stores.get_store(value).visit_sp_not_has_concern())
			if cant > 0:
				ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td><td>"+str(cant)+"</td></tr>"
		ans += "</table><br>"
		return ans

	def resume_store(self,store):
		ans = "<h4>Información de la tienda</h4>"
		ans += "<table>"
		ans += "<tr><th>Gerente</th><th>Celular</th><th>Anexo</th><th>Telefono</th><th>Gerente Regiónal</th></tr>"
		ans += "<tr><td>"+store.info.manager+"</td>"+"<td>"+store.info.cellphone+"</td>"
		ans += "<td>"+store.info.annexed+"</td>"+"<td>"+store.info.phone+"</td><td>"+store.info.regional_manager+"</tr>"
		ans += "<tr><th>Direccion</th><td colspan='4'>"+store.info.direction+"</td></tr>"
		ans += "</table><br>"

		ans += "<table>"
		ans += "<tr><th>Cantidad Visitas</th><td>"+str(len(store.visits))+"</td>"
		ans += "<th>Calificación promedio</th><td>"+str(store.avg_qualification())+"</td></tr>"
		ans += "</table>"
		ans += "<h4>Resumen cantidad de recibidores</h4>"
		ans += "<table><tr>"
		receiv = store.count_receivers()
		for value in receiv:
			ans += "<td>"+value+"</td>"
		ans += "</tr><tr>"
		for value in receiv:
			ans += "<td>"+str(receiv[value])+"</td>"
		ans += "</tr>"
		ans += "</table>"
		ans += "<h4>Resumen Horarios</h4>"
		good_schedule = store.count_good_schedule()
		bad_schedule = store.count_bad_schedule()
		ans += "<table><th>Horario</th>"
		for value in good_schedule:
			ans += "<td align='center'>"+value+"</td>"
		ans += "</tr><tr><th>Mal Horario</th>"
		for value in good_schedule:
			ans += "<td>"+str(bad_schedule[value])+"</td>"
		ans += "</tr><tr><th>Buen Horario</th>"
		for value in good_schedule:
			ans += "<td>"+str(good_schedule[value])+"</td>"
		ans +="</tr></table>"


		return ans

	def cant_refrigerator(self, cant):
		if cant == -1:
			return "Sin información"
		else:
			return str(cant)

	def info_visit(self, visit):
		formato = "%d / %m / %Y"
		options = {1:'Sí', 0:'No'}

		ans = "<table>"
		ans += "<tr><th>Fecha</th><td>"+visit.date.strftime(formato)+"</td>"
		ans += "<th>Calificación</th><td>"+str(visit.qualification)+"</td></tr>"

		ans += "<tr><th>Horario Visita</th><td>"+visit.schedule.name+"</td>"
		ans += "<th>Buen Horario</th><td>"+options[visit.schedule.good]+"</td></tr>"
		ans += "<th>Recibidores</th><td>"
		i = 0
		for value in visit.receivers:
			if i != 0:
				ans += ", "
			ans += value
			i += 1
		ans += "</td><th>Tenía Branding</th><td>"+options[visit.waters.branding.has_branding]+"</tr><tr>"
		ans += "<th>Refrigerador funcionaba</th><td>"+options[visit.waters.refrigerator.working]+"</td>"
		ans += "<th>Refrigerador estaba limpio</th><td>"+options[visit.waters.refrigerator.clean]+"</td></tr>"
		ans += "<tr><th>Refrigerador estaba visible</th><td>"+options[visit.waters.refrigerator.visible]+"</td>"
		ans += "<th>Cantidad Refrigeradores</th><td>"+self.cant_refrigerator(visit.quantity_refrigerator())+"</td></tr>"
		ans += "<tr><th>Refrigerador tenía encargado</th><td>"+options[visit.waters.refrigerator.concern]+"</td>"
		ans += "<th>Refrigerador tenía stock </th><td>"+options[visit.waters.refrigerator.stock]+"</td></tr>"
		ans += "<tr><th>Producto Solidario tenía stock</th><td>"+options[visit.solidarity_product.stock]+"</td>"
		ans += "<th>Producto Solidario tenía encargado</th><td>"+options[visit.solidarity_product.concern]+"</td></tr>"
		ans += "<tr><th>Comentarios</th><td colspan='3'>"+visit.comments+"</td></tr>"
		ans += "</table>"
		return ans

	def info_receivers_stores(self,stores):
		ans = "<table>"
		ans += '<tr><th colspan="3">Zona Norte</th><tr>'
		ans += '<tr><th>Tienda</th><th>Visitas</th><th>Veces jefe tienda</th></tr>'
		for value in stores.norte_visited:
			receivers = stores.get_store(value).count_receivers()
			ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
			ans += "<td>"+str(stores.get_store(value).cant_visits())+"</td>"
			ans += "<td>"+str(receivers["Jefe de tienda"])+"</td></tr>"
		ans += '</table><br>'

		ans += '<table>'
		ans += '<tr><th colspan="3">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Visitas</th><th>Veces jefe tienda</th></tr>'
		for value in stores.norte_visited:
			receivers = stores.get_store(value).count_receivers()
			ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
			ans += "<td>"+str(stores.get_store(value).cant_visits())+"</td>"
			ans += "<td>"+str(receivers["Jefe de tienda"])+"</td></tr>"
		ans += '</table><br>'

		ans += '<table>'
		ans += '<tr><th colspan="3">Región Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Visitas</th><th>Veces jefe tienda</th></tr>'
		for value in stores.norte_visited:
			receivers = stores.get_store(value).count_receivers()
			ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
			ans += "<td>"+str(stores.get_store(value).cant_visits())+"</td>"
			ans += "<td>"+str(receivers["Jefe de tienda"])+"</td></tr>"
		ans += '</table><br>'

		ans += '<table>'
		ans += '<tr><th colspan="3">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Visitas</th><th>Veces jefe tienda</th></tr>'
		for value in stores.norte_visited:
			receivers = stores.get_store(value).count_receivers()
			ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
			ans += "<td>"+str(stores.get_store(value).cant_visits())+"</td>"
			ans += "<td>"+str(receivers["Jefe de tienda"])+"</td></tr>"
		ans += '</table><br>'

		return ans

	def info_schedule_visits(self,stores):
		ans = "<h4>Zona norte</h4>"
		good_schedule = stores.good_schedule_norte()
		bad_schedule = stores.bad_schedule_norte()
		ans += "<table>"
		ans += "<tr><th>Horario</th><th>Buen horario</th><th>Mal horario</th></tr>"
		for value in good_schedule:
			ans += "<tr>"
			ans += "<td>"+value+"</td>"
			ans += "<td>"+str(good_schedule[value])+"</td>"
			ans += "<td>"+str(bad_schedule[value])+"</td>"
			ans += "</tr>"
		ans += "</table>"

		ans += "<h4>Zona centro</h4>"
		good_schedule = stores.good_schedule_centro()
		bad_schedule = stores.bad_schedule_centro()
		ans += "<table>"
		ans += "<tr><th>Horario</th><th>Buen horario</th><th>Mal horario</th></tr>"
		for value in good_schedule:
			ans += "<tr>"
			ans += "<td>"+value+"</td>"
			ans += "<td>"+str(good_schedule[value])+"</td>"
			ans += "<td>"+str(bad_schedule[value])+"</td>"
			ans += "</tr>"
		ans += "</table>"

		ans += "<h4>Región Metropolitana</h4>"
		good_schedule = stores.good_schedule_rm()
		bad_schedule = stores.bad_schedule_rm()
		ans += "<table>"
		ans += "<tr><th>Horario</th><th>Buen horario</th><th>Mal horario</th></tr>"
		for value in good_schedule:
			ans += "<tr>"
			ans += "<td>"+value+"</td>"
			ans += "<td>"+str(good_schedule[value])+"</td>"
			ans += "<td>"+str(bad_schedule[value])+"</td>"
			ans += "</tr>"
		ans += "</table>"

		ans += "<h4>Zona sur</h4>"
		good_schedule = stores.good_schedule_sur()
		bad_schedule = stores.bad_schedule_sur()
		ans += "<table>"
		ans += "<tr><th>Horario</th><th>Buen horario</th><th>Mal horario</th></tr>"
		for value in good_schedule:
			ans += "<tr>"
			ans += "<td>"+value+"</td>"
			ans += "<td>"+str(good_schedule[value])+"</td>"
			ans += "<td>"+str(bad_schedule[value])+"</td>"
			ans += "</tr>"
		ans += "</table>"

		return ans
