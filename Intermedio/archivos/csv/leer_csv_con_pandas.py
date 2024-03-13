import pandas as pd

# Usando la función read_csv para leer archivos CSV
data_frame = pd.read_csv("datos.csv")
data_frame2 = pd.read_csv("datos.csv")

# Obteniendo los datos de la columna nombre
nombres = data_frame["nombre"]

# Ordenando el dataframe por edad
df_ordenado_ascendente = data_frame.sort_values("edad")

# ordenandolo de forma descendente
df_ordenado_descendente = data_frame.sort_values("edad", ascending=False)

# Concatenando los 2 dataframes
df_concatenado = pd.concat([data_frame, data_frame2])

# Accediendo a las 2 primeras filas con head()
primeras_fila = data_frame.head(2)

# Accediendo a las ultimas filas con tail()
ultimas_filas = data_frame.tail(2)

# Accediendo a la cantidad de filas y columnas con shape
# filas_y_columnas_totales = data_frame.shape # Devulve una tupla
# filas_totales = filas_y_columnas_totales[0]
# columnas_totales = filas_y_columnas_totales[1]
# Desempaquetando
filas_totales, columnas_totales = data_frame.shape

# Obteniendo data estadistica del dataframe:
df_info = data_frame.describe()

# Accediendo al nombre de la fila 2 loc
elementos_especificos_loc = data_frame.loc[2,"nombre"]

# Accediendo al nombre de la fila 2 con iloc
elementos_especificos_iloc = data_frame.iloc[2,0]

# Accediendo a todos los apellidos con loc
apellidos_loc = data_frame.loc[:,"apellido"]

# Accediendo a todos los apellidos con iloc
apellidos_iloc = data_frame.iloc[:,1]

# Accediendo a la fila 3 con loc
fila_3 = data_frame.loc[2,:]

# Accediendo a la fila 3 con iloc
fila_4 = data_frame.iloc[3,:]

# Accediendo a filas con edad mayor a 30
mayor_que_30 = data_frame.loc[data_frame["edad"]>30,:]

print(mayor_que_30)



