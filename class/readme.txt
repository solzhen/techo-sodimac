Para arrancar la aplicacion:

$ pip3 install -r requirements.txt

$ python3 app.py

(puede ser python y pip en su defecto)

app.py es la aplicacion web, esta depende de las clases almacenadas en el archivo class

INFORMACION DE LAS CLASES:

Connection: se conecta con gogogle, requiere de un nombre de documento (de drive) y de una
	llave cliente secreto json

Querys: realiza las consultas, requiere de un objeto Conection y de un objeto List_Stores
	Basicamente tiene un metodo que realiza las consultas entre "n" dias: del dia de hoy, hasta
	n dias para atras y muta el objeto List_Stores con la informacion

List_Stores: Contiene la lista de todas las tiendas visitadas y no visitadas.

Store: Informacion de cada Store. Nombre, lista de visitas (Visit) 
	e informacion de cadatienda (Info_Store)

Info_Store: nombre, encargado, celular, anexo, numero de telefono, encargado regional y direccion
	de cada tienda

Visit: informacion de cada visita. Fecha, Recibidores, Calificacion, Comentarios, informacion
	relativa al agua (Water), producto solidario (Solidarity_Product) y horario (Schedule)

Water: informacion del refrigerador (Refrigerator) y del branding (Branding)

Refrigerator: informacion acerca de si estaba limpio, en funcionamiento, visible, tenia stock, 
	tenia encargado, y la cantidad de refrigeradores

Branding: informacion acerca si tenia branding, si lucia bien, si estaba limpio y si se veia nuevo

Solidarity_Product: informacion acerca si tenia stock y si tenia encargado

Schedule: nombre del horario y si era bueno o no.

tables: genera strings con tablas para mostrar en app.py. 



Cuando la aplicacion se inicializa, pide el numero de dias y luego calcula todo con respecto
a ese numero de dias. Se conecta con Connection, y Querys muta el objeto List_Stores creado.
Luego se hacen las consultas a la List_Stores usando los metodos de este objeto.