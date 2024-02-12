# Lista
lista = ["Mateo Congo", "Soy Afordesendiente", True, 1.80]

print(f" Tercer elemento de la lista antes de modificar, {lista[2]}")

# Modificacndo el tercer elemento de la lista
lista[2] = False

print(f" Tercer elemento de la lista DESPUES de modificar, {lista[2]}")

# La tupla no se puede modificar
tupla = ("Mateo Congo", "Soy Afordesendiente", True, 1.80)

# Creación de un conjunto
# No pueden existir datos duplicados y no se pueden acceder a elementos por indice
conjunto = {"Mateo Congo", "Soy Afordesendiente", True, 1.80}

# print(conjunto[3]) -> no se puede acceder al elemento

# Creando un diccionario
# La estructura del diccionario es clave (key) y valor (value) y los separamos por comas
diccionario = {
    # key    :  value
    "nombre": "Mateo Congo",
    "edad" : 22,
    "genero": "masculino",
    "altura" : 1.80,
    "estado_civil" : "soltero"
}

print(f"Presentar el estado civil del involucrado: {diccionario["estado_civil"]}")