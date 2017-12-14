import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as ps
from datetime import datetime, date, time, timedelta


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Visitas Sodimac (Responses)").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
df = ps.DataFrame(sheet.get_all_records())

tiendas_norte = {"NORTE-  Hc Antofagasta- Balmaceda Nº 2355, Interior Recinto Portuario Extremo Sur, dentro del Mall, Antofagasta":0,
                "NORTE- Hc Iquique Héroes de la Concepción Nº 2311, Iquique":0,
                "NORTE- Hc Calama Balmaceda Nº 3398, Calama":0,
                "NORTE 4 Hc Arica Av. Santa María Nº 2985, Arica":0,
                "NORTE Co Antofagasta- Av. Antonio Rendic Nº 6852, Antofagasta":0,
                "NORTE HC Alto Hospicio- Av. Los Aromos Nº 2780, Alto Hospicio":0,
                "NORTE Hc Copiapó Cordillera- Av. Los Carrera 4723, Copiapó":0}

tiendas_centro = {"CENTRO- Co Viña del Mar Limache Nº 3119, Viña del Mar":0,
                 "CENTRO- Hc Viña del Mar 15 Norte Nº 961, Viña del Mar":0,
                 "CENTRO- Co Rancagua Koke Nº 011, Rancagua":0,
                 "CENTRO- Co Valparaíso Yungay Nº 2516, Valparaíso":0,
                 "CENTRO- Hc La Serena Av. Fco. de Aguirre Nº 02, La Serena":0,
                 "CENTRO- Hc Rancagua Av. Albert Einstein Nº 297, Rancagua":0,
                 "CENTRO- Hc El Belloto Avenida Freire Nº 1351, Quilpué":0,
                 "CENTRO- Hc Reñaca Alessandri Nº 4085, Reñaca Alto, Viña del Mar":0,
                 "CENTRO- Hc Coquimbo- Ruta 5 Norte Nº 849, Coquimbo":0,
                 "CENTRO- Hc Quinta Vergara Av. Valparaíso Nº 1070, Viña del Mar":0}

tiendas_sur = {"SUR- Hc Concepción Los Carrera Nº 1175, Concepción":0,
              "SUR- Hc Osorno René Soriano Nº 2619, Osorno":0,
              "SUR- Hc Los Angeles Av. Alemania Nº 850, Los Angeles":0,
              "SUR- Hc Valdivia Av. Picarte Nº 3349, Valdivia":0,
              "SUR- Hc Puerto Montt Av. Presidente Ibañez Nº 650, Puerto Montt":0,
              "SUR- Hc Temuco Cautín Caupolicán Nº 0457, Temuco":0,
              "SUR- Hc Mall Plaza El Trébol Av. Pdte. Jorge Alessandri Nº 3177, Concepción":0,
              "SUR- Hc Autopista Talcahuano Autopista Concep-Talcahuano Nº 9200, comuna Hualpén, Talcahuano":0,
              "SUR- Hc Mall Bío Bío Av. Los Carreras Poniente Nº 301, Concepción":0}

tiendas_rm = {"RM- Hc San Miguel Gran Avda. José Miguel Carrera Nº 5508, San Miguel, Santiago":0,
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

formato_fecha = "%m/%d/%Y %H:%M:%S"
hoy = datetime.today()

tiendas = {}
sur = {}
norte = {}
centro = {}
rm = {}


for index, rows in df.iterrows():
    fecha = datetime.strptime(df['Timestamp'][index],formato_fecha)
    if (hoy - fecha).days < 31:
        tienda_actual = df['Tienda visitada (agregado)'][index]
        if tienda_actual in tiendas:
            tiendas[tienda_actual] += 1
            
        else:
            tiendas[tienda_actual] = 1

        if tienda_actual.startswith('NOR'):
            if tienda_actual in norte:
                norte[tienda_actual] += 1
            else:
                norte[tienda_actual] = 1
        
        elif tienda_actual.startswith("SUR"):
            if tienda_actual in sur:
                sur[tienda_actual] += 1
            else:
                sur[tienda_actual] = 1
                
        elif tienda_actual.startswith("CEN"):
            if tienda_actual in centro:
                centro[tienda_actual] += 1
            else:
                centro[tienda_actual] = 1
        
        elif tienda_actual.startswith("RM"):
            if tienda_actual in rm:
                rm[tienda_actual] += 1
            else:
                rm[tienda_actual] = 1

total_tiendas = len(tiendas_rm)+len(tiendas_sur)+len(tiendas_centro)+len(tiendas_norte)
tiendas_faltantes =total_tiendas - len(tiendas)

print("Tiendas visitadas el ultimo mes: "+str(len(tiendas)))

print("Tiendas Faltaltes por visitar: "+str(tiendas_faltantes))