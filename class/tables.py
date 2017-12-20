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
		ans += '<tr><th>Tienda</th><th>Promedio Calificacion</th><th>Visitas</th></tr>'
		for value in stores.norte_visited:
			ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
			ans += "<td>"+str(stores.norte_visited[value].avg_qualification())+"</td>"
			ans += "<td>"+str(stores.norte_visited[value].cant_visits())+"</td></tr>"
		ans += '</table><br>'

		ans += '<table>'
		ans += '<tr><th colspan="3">Zona Centro</th><tr>'
		ans += '<tr><th>Tienda</th><th>Promedio Calificacion</th><th>Visitas</th></tr>'
		for value in stores.centro_visited:
			ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
			ans += "<td>"+str(stores.centro_visited[value].avg_qualification())+"</td>"
			ans += "<td>"+str(stores.centro_visited[value].cant_visits())+"</td></tr>"
		ans += '</table><br>'

		ans += '<table>'
		ans += '<tr><th colspan="3">Region Metropolitana</th><tr>'
		ans += '<tr><th>Tienda</th><th>Promedio Calificacion</th><th>Visitas</th></tr>'
		for value in stores.rm_visited:
			ans += "<tr><td><a href =./info_store?st="+self.parse_link(value)+">"+value+"</a></td>"
			ans += "<td>"+str(stores.rm_visited[value].avg_qualification())+"</td>"
			ans += "<td>"+str(stores.rm_visited[value].cant_visits())+"</td></tr>"
		ans += '</table><br>'

		ans += '<table>'
		ans += '<tr><th colspan="3">Zona Sur</th><tr>'
		ans += '<tr><th>Tienda</th><th>Promedio Calificacion</th><th>Visitas</th></tr>'
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
		ans += '<tr><th colspan="3">Region Metropolitana</th><tr>'
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
		ans += '<tr><th colspan="2">Region Metropolitana</th><tr>'
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
		ans += '<tr><th colspan="2">Region Metropolitana</th><tr>'
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
		ans += '<tr><th colspan="2">Region Metropolitana</th><tr>'
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
		ans += '<tr><th colspan="2">Region Metropolitana</th><tr>'
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
		ans += '<tr><th colspan="2">Region Metropolitana</th><tr>'
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
		ans += '<tr><th colspan="2">Region Metropolitana</th><tr>'
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
		ans += '<tr><th colspan="2">Region Metropolitana</th><tr>'
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
		ans = "<table>"
		ans += "<tr><th>Cantidad Visitas</th><td>"+str(len(store.visits))+"</td>"
		ans += "<th>Calificacion promedio</th><td>"+str(store.avg_qualification())+"</td></tr>"
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


	def info_visit(self, visit):
		formato = "%d de %B - %Y"
		options = {1:'Sí', 0:'No'}
		ans = "<table>"
		ans += "<tr><th>Fecha</th><td>"+visit.date.strftime(formato)+"</td>"
		ans += "<th>Calificacion</th><td>"+str(visit.qualification)+"</td></tr>"

		ans += "<tr><th>Horario Visita</th><td>"+visit.schedule.name+"</td>"
		ans += "<th>Buen Horario</th><td>"+options[visit.schedule.good]+"</td></tr>"
		ans += "<th>Recibidores</th><td>"
		i = 0
		for value in visit.receivers:
			if i != 0:
				ans += ", "
			ans += value
			i += 1
		ans += "</td>"
		ans += "<th>Refrigerador funcionaba</th><td>"+options[visit.waters.refrigerator.working]+"</td></tr>"
		ans += "<tr><th>Refrigerador estaba limpio</th><td>"+options[visit.waters.refrigerator.clean]+"</td>"
		ans += "<th>Refrigerador estaba visible</th><td>"+options[visit.waters.refrigerator.visible]+"</td></tr>"
		ans += "<tr><th>Refrigerador tenía encargado</th><td>"+options[visit.waters.refrigerator.concern]+"</td>"
		ans += "<th>Refrigerador tenia stock </th><td>"+options[visit.waters.refrigerator.stock]+"</td></tr>"
		ans += "<tr><th>Producto Solidario tenia stock</th><td>"+options[visit.solidarity_product.stock]+"</td>"
		ans += "<th>Producto Solidario tenia encargado</th><td>"+options[visit.solidarity_product.concern]+"</td></tr>"
		ans += "<tr><th>Comentarios</th><td colspan='3'>"+visit.comments+"</td></tr>"
		ans += "</table>"
		return ans