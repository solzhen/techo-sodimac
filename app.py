import sys
sys.path.append('class')
from datetime import datetime, date, time, timedelta
from Connection import *
from Store import *
from Querys import *
from List_Stores import *
from tables import *

import cherrypy


class Sodimac(object):
    def __init__(self):
      self.stores = None
      self.days = 1
      self.tables = Tables()

    @cherrypy.expose
    def index(self):
      
      return """<html>
          <head></head>
          <body>
            <form method="get" action="generate_db">
              <input type="number" value="40" name="days" />
              <button type="submit">Ingrese Numero de Dias</button>
            </form>
            </body>
          </html>"""

    @cherrypy.expose
    def generate_db(self, days):
      self.days = days
      connection = Connection("Visitas Sodimac (Responses)", 'client_secret.json')
      sheet1 = connection.get_sheet1()

      df = ps.DataFrame(sheet1.get_all_records())

      self.stores = List_Stores()

      querys = Query(df, self.stores)
      querys.query_date(int(days))

      return self.visited_stores()

    @cherrypy.expose
    def visited_stores(self):
      
      ans = self.header()
      ans += "<h3>Tiendas visitadas: "+str(self.stores.total_visited())+"<h3>"
      ans += self.tables.visited_stores(self.stores)
      ans += """</body>
            </html>"""
      return ans


    @cherrypy.expose
    def not_visited_stores(self):
      ans = self.header()
      ans += "<h3>Tiendas no visitadas: "+str(self.stores.not_total_visited())+"<h3>"
      ans += self.tables.not_visited_stores(self.stores)
      ans += """</body>
              </html>"""
      return ans

    @cherrypy.expose
    def refrigerators(self):
      ans = self.header()
      ans += "<h2>Refrigeradores sucios</h2>"
      ans += self.tables.refrigerators_not_clean(self.stores)
      ans += "<h2>Refrigeradores no funcionando</h2>"
      ans += self.tables.refrigerators_not_working(self.stores)
      ans += "<h2>Refrigeradores no visibles </h2>"
      ans += self.tables.refrigerators_not_visible(self.stores)
      ans += """</body>
              </html>"""
      return ans

    @cherrypy.expose
    def water(self):
      ans = self.header()
      ans += "<h2>Agua sin stock</h2>"
      ans += self.tables.water_has_not_stock(self.stores)
      ans += "<h2>Agua sin encargado</h2>"
      ans += self.tables.water_has_not_concern(self.stores)
      ans += """<body>
              </html>"""
      return ans

    @cherrypy.expose
    def social_product(self):
      ans = self.header()
      ans += "<h2>Producto social sin stock</h2>"
      ans += self.tables.ps_has_not_stock(self.stores)
      ans += "<h2>Producto social sin encergado</h2>"
      ans += self.tables.ps_has_not_concern(self.stores)
      ans += """<body>
              </html>"""
      return ans

    @cherrypy.expose
    def info_store(self,st):
      store = self.stores.get_store(self.tables.reverse_parse_link(st))
      ans = self.header()
      ans += "<h2>"+store.name+"</h2><br>"
      ans += self.tables.resume_store(store)
      ans += "<h3>Visitas:</h3>"
      for value in store.visits:
        ans += self.tables.info_visit(store.visits[value])

      return ans

    @cherrypy.expose
    def receivers(self):
      ans = self.header()
      ans += "<h3>Cantidad de veces que estuvo jefe de tienda</h3>"
      ans += self.tables.info_receivers_stores(self.stores)

      return ans

    @cherrypy.expose
    def schedules(self):
      ans = self.header()
      ans += self.tables.info_schedule_visits(self.stores)

      return ans

    def header(self):
      hoy = datetime.today()
      formato = "%d-%m-%Y"
      ans = """<html>
          <head>
          <style>
              table {
                  font-family: arial, sans-serif;
                  border-collapse: collapse;
                  width: 95%
              }
              ul.horizontal{
              margin:0;
              padding:0;
              }

              ul.horizontal li{
              display:block;
              float:left;
              padding:0 10px;
              }

              td, th {
                  border: 1px solid #dddddd;
                  text-align: left;
                  padding: 2px;
              }

              tr:nth-child(even) {
                  background-color: #dddddd;
              }
              </style>
            </head>
          <body>
          <ul  class="horizontal">
            <li><a href="./index"> Inicio</a></li>
            <li><a href="./visited_stores">Tiendas Visitadas</a></li>
            <li><a href="./not_visited_stores">Tiendas No Visitadas</a></li>
            <li><a href="./water">Agua</a></li>
            <li><a href="./social_product">Producto Solidario</a></li>
            <li><a href="./receivers">Recibidores</a></li>
            <li><a href="./schedules">Horario Visitas </a></li>
          </ul>
          <br>

           """
      ans += "  Consulta realizada entre los dias "+hoy.strftime(formato)
      ans += " y "+(hoy - timedelta(days=int(self.days))).strftime(formato)
      return ans



        


if __name__ == '__main__':
  cherrypy.config.update({'server.socket_host': '0.0.0.0',})
  cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
  cherrypy.quickstart(Sodimac())