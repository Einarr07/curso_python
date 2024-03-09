# Falto el profesor y 2 alumnos van a hacer la clase
# A) Pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de mayor a menor
# B) El mayor es el profesor y el menor es el asistente: ¿Quién es?

# Pedimos el total de compañeros para saber cuantos datos vamos a ingresar
total_compañeros = int(input("¿Cuántos compañeros son?: "))

# Creamos una lista vacia y un indice 0
lista_compañeros = []
i = 0

# Iteramos e ingresamos las edades de todos los compañeros mientras las agregamos a una lista
while i < total_compañeros:
    i += 1
    edad = int(input(f"Ingresa la edad del compañero {i}: "))
    lista_compañeros.append(edad)

# Ordenamos la lista de forma descendente
lista_compañeros.sort(reverse=True)
# Resultado A
print(f"Las edades de los compañeros en orden desendente es:\n{lista_compañeros}")

edad_profesor = max(lista_compañeros)
edad_asistente = min(lista_compañeros)

# Resultado B
print(f"El compañero que sera el profesor tiene {edad_profesor} años y el asistente {edad_asistente} años")
