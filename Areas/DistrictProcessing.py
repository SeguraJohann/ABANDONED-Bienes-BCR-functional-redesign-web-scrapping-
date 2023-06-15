import pandas as pd
import psycopg2
from psycopg2 import Error


#Creates a df the Province column only, deletes duplicates values and reset the indexes from 1 to 7

data = pd.read_csv('Districts_of_Costa_Rica_1.csv')
provincias = pd.DataFrame(data['Province'].copy())
provincias = provincias.drop_duplicates()
provincias = provincias.reset_index(drop=True)
provincias.index = provincias.index + 1
provincias['Index'] = provincias.index


#Creates a df the Canton column only, deletes duplicates values and reset the indexes and add it as a column

canton = data[['Province','Canton']].copy()
canton = canton.drop_duplicates()
canton = canton.reset_index(drop=True)
canton.index = canton.index + 1
canton['Index'] = canton.index


#Creates a df the districts column only, deletes duplicates values and reset indexes

district = data[['Canton','District']].copy()
district = district.drop_duplicates()
district = district.reset_index(drop=True)
district.index = district.index + 1

for _, values in provincias.iterrows():
    canton.loc[canton['Province'] == values['Province'],'Province'] = values['Index']

#print(canton)

for _, values in canton.iterrows():
    district.loc[district['Canton'] == values['Canton'],'Canton'] = values['Index']
''' tests
print(district)
print("Cantones")
for _, values in canton.iterrows():
    print(values["Canton"], values["Index"])
'''

####Postgrest######


try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="Tests1",
        user="postgres",
        password="EstaEsLaDePostgre1508"
    )

except (Exception, Error) as error:
    print("Error al conectar a la base de datos:", error)

cursor = conn.cursor()
sql = 'SELECT * FROM "Provincias"'
cursor.execute(sql)
results = cursor.fetchall()

print(provincias)
tablaProvincia = '"Provincias"'
tablaCanton = '"cantones"'
tablaDistrito = '"distritos"'

#Insert Province
for index, row in provincias.iterrows():
    provincia = row["Province"]
    id_provincia = row["Index"]

    # Crear la consulta SQL para insertar los datos
    consulta = f"INSERT INTO {tablaProvincia} (id, name) VALUES ({id_provincia}, '{provincia}')"

    # Ejecutar la consulta
    cursor.execute(consulta)
#Insert Canton
'''
for index, row in provincias.iterrows():
    provincia = row["Province"]
    id_provincia = row["Index"]

    # Crear la consulta SQL para insertar los datos
    consulta = f"INSERT INTO {tablaProvincia} (id, name) VALUES ({id_provincia}, '{provincia}')"

    # Ejecutar la consulta
    cursor.execute(consulta)'''

conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()