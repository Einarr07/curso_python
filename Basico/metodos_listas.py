# Función crear una lista con list()
lista = list(["hola", "juan", 23,56,85,True])

# Devuelve la cantidad de elementos a la lista
cantidad_elementos = len(lista)
print(f"La cantidad de elementos que existen en la lista son:  {cantidad_elementos}")

# Agregando un elemento a la lista con append()
# Se agg el final de la lista
lista.append("Stuard")

# Agregando un elemento a la lista en un indice especifico
lista.insert(2, "Marco")

# Agregamos varios elementos a la lista con extend()
lista.extend([False, 546, 987, "Lista 2"])

# Eliminando un elemento de la lista  con pop() por un indice
lista.pop(0)

# Para eliminar los ultimos elementos de la lista utilizamos -1 para eliminar el ultimo, -2 para el ante ultimo, etc.
lista.pop(-1)

# Removiendo un elemento de la lista por su valor con remove() ç
lista.remove(546)

lista2 = [123,654,987,51,321,87,54,321,6874,]
# Ordenando los elementos de una lista (Esto solo funciona con numeros o valores booleanos)
# Si utilizamos el valor sort(reverse=True) los ordenamos de forma descendente (De mayor a menor)
lista2.sort()

# Invertimos los elementos de una lista
lista.reverse()

# Eliminar todos los elementos de la lista
# lista.clear()

print(lista)
print(lista2)