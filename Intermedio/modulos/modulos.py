# Importando un modulo y asignandole el nombre: "m_saludar"
# import modulo_saludar as m_saludar

# Desde ese modulo, importamos 2 funciones
from modulo_saludar import saludar, saludar_raro

# Creamos las variables con saludos
saludo = saludar(input("Ingresa tu nombre: "))
saludo_raro = saludar_raro(input("Ingresa tu nombre para un saludo raro: "))

# Mostramos los resultados
print(saludo)
print(saludo_raro)

# Para ver las propiedades y metodos de el namespace
# print(dir(m_saludar))

# Accedemos al nombre del modulo
print(__name__)

# Accedemos al nombre del modulo llamado
# print(m_saludar.__name__)