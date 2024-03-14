import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo csv
df = pd.read_csv("comida.csv")

# Creando el grafico lineal
sns.lineplot(x="fecha",y="cantidad_comida",data=df)

# Obteniendo el indice del valor maximo en la columna "cantidad_comida"
indice_maximo = df["cantidad_comida"].idxmax()

# Obtener la fecha y la cantidad correspondiente al máximo
fecha_maxima, cantidad_maxima = df.loc[indice_maximo, ["fecha", "cantidad_comida"]]

# Agregar un punto en la línea más alta
plt.plot(fecha_maxima, cantidad_maxima, 'ro', markersize=10)

# Mostrar el gráfico
plt.show()