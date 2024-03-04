diccionario = {
    "materia": "Aplicaciones moviles",
    "estado": "cursando",
    "nota b1": 8.25,
    "nota b2": 7.30
}

# Nos muestra solo las claves
for key in diccionario:
    print(key)

# Obtenemos las claves y los valores
for datos in diccionario.items():
    clave = datos[0]
    valor = datos[1]
    print(f"La clave es: {clave} y el valor es: {valor}")