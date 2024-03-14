import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo csv
df = pd.read_csv("cofla_ingresos.csv")

# Creando el grafico lineal
sns.barplot(x="fuente",y="ingresos",data=df)

# Obteniendo el total de ingresos
total_ingresos = df["ingresos"].sum()

# Mostrando el total
print(f"El total de los ingresos de cofla es: ${total_ingresos} USD")

# Mostrar el gráfico
plt.show()