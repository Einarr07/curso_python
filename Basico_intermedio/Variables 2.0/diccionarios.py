# Creamos un diccionario con dic()
diccionario = dict(pais="Ecuador", provincia="Pichincha")

# Las listas no pueden ser claves y usamos frozenset  para meter conjuntos
diccionario = {frozenset(["ciudad", "capital"]): "Quito"}

# Creamos un diccionario con fromkeys()
# Esto hace que podamos crear claves con todos los valores NONE
diccionario = dict.fromkeys(["pais","provincia","capital"])

# fromkeys() con dos parametros
diccionario = dict.fromkeys("ABCDEFG", "letra")

print(diccionario)