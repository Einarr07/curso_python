diccionario = {
    "Nombre": "Fernando",
    "Apellido": "Palomino",
    "Edad": 56
}

# Devuelve las claves del diccionario (Tambien sirve para iterar)
claves = diccionario.keys()

# Obtenemos un elemento con un get() (valor)
valor = diccionario.get("Apellido")

# Elimminando un elemento del diccionario se hace mediante la key
diccionario.pop("Nombre")

# Obteniendo un elemento dict_items iterable (Recorrer el elemento)
diccionario_iterable = diccionario.items()

# Elimina todos los elementos del diccionario
# diccionario.clear()

print(diccionario)
print(diccionario_iterable)