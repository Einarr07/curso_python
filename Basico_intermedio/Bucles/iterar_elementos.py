# Todo lo mostrado acontinuación funciona tanto como para listas[], tuplas() y conjuntos{}

animales = ["perro", "gato", "loro", "cerdo", "pez"]
numeros = [5,6,68,47,5.3]

# Recorriendo la lista animales
for animal in animales:
    print(f"La variable animal es igual a: {animal}")

# Rcorriendo la lista numeros y multiplicando por 2
for numero in numeros:
    resultado = numero * 2
    print(f"{resultado}")

# Para iterar 2 listas, estas deben tener la misma cantidad de elementos

for animal, numero in zip(animales, numeros):
    print(f"Lista 1: {animal}")
    print(f"Lista 2: {numero}")

# Recorriendo numeros en un rango
for num in range(5, 10):
    print(f"Iterando en un rango de números: {num}")

# Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")

# Usando el else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else: # El else siempre se va a ejecutar
    print("El blucle se termino")
