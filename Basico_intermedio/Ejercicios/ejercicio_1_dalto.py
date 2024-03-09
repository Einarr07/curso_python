# Falto el profe y los pibes van a armar la clase.

# Función para obtener al asistente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):

    # Creamos la lista de compañeros
    compañeros = []

    # Ejecutando un for para pedir información de cada compañero
    for i in range(cantidad_de_compañeros):
        i += 1
        nombre = input(f"Ingresa el nombre del compañero {i}: ")
        edad = int(input(f"Ingresa la edad del compañero {i}: "))
        compañero = (nombre, edad)

        # Agregando la información a la lista
        compañeros.append(compañero)

    # Ordenandolos de menor a mayor según su edad
    compañeros.sort(key = lambda x:x[1])

    # Compañeros[x] devuelve una tupla con (nombre, edad) y después accedemos al nombre
    # Para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]

    # Retornamos una tupla
    return asistente, profesor


# Desempaquetamos lo que nos retorna la función
total_compañeros = int(input("¿Cuántos compañeros son?: "))
asistente, profesor = obtener_compañeros(total_compañeros)

# Mostramos el resultado
print(f"El profesor es: {profesor} y su asistente es: {asistente}")