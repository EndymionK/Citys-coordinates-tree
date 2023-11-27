import pandas as pd

# Lee el archivo CSV
file_path = "C:\Proyectos programación\Citys-coordinates-tree\Databases\worldcitiespop.csv"  # Reemplaza "tu_archivo.csv" con la ruta real de tu archivo CSV
data = pd.read_csv(file_path)

# Muestra las primeras filas del DataFrame original
print("DataFrame Original:")
print(data.head())

# Elimina las columnas especificadas
columns_to_drop = ['Country', 'AccentCity', 'Region', 'Population']
data = data.drop(columns=columns_to_drop)

# Elimina las filas duplicadas basadas en latitud y longitud
data = data.drop_duplicates(subset=['Latitude', 'Longitude'])

# Muestra las primeras filas del DataFrame modificado
print("\nDataFrame Modificado:")
print(data.head())

# Guarda el DataFrame modificado en un nuevo archivo CSV si es necesario
data.to_csv("cleardata.csv", index=False)  # Descomenta esta línea para guardar el DataFrame modificado
