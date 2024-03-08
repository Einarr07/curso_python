# Creamos una función con 3 parametros
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, como estas {adjetivo}?"


frase_resultante = frase("Alexander", "Toapanta", "maquinola")
print(frase_resultante)


# Creando una función con un parametro opcional y un valor por defecto
def compras(comestible, bebida = "Monster"):
    return f"Hoy compre {comestible} y un {bebida} para almorzar"


frase_compras = compras("arroz")
print(frase_compras)