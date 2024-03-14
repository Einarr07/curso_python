# Cambiar los tipos de datos de una columna
import pandas as pd

df = pd.read_csv("datos.csv")

# Convertir a str lso datos de una columna
df["edad"] = df["edad"].astype(str)

# Mostrando el tipo de dato del primer elemento de la columna edad
# print(type(df["edad"][0]))

# Reemplazando el dato "michael" por "mishell"
df.replace({"nombre": {"michael": "mishell"}}, inplace=True)

#print(df,"\n")

# Eliminando las filas con datos vacios
df = df.dropna() # si queremos eliminar columnas utilisamos df.dropna(axis=1)

#print(df,"\n")

# Eliminando las filas repetidas
df = df.drop_duplicates()

print(df)

# Creando un CSV con el dataframe resultante (limpio)
df.to_csv("datos_limpios.csv")


