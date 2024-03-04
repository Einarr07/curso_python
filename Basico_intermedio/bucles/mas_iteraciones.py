# Creando las listas
ingredientes_pastel = ["harina", "azucar", "celular", "polvo de hornear", "bicarbonato de sodio", "1 cucharadita de sal",
                       "mantequilla", "huevos", "leche","extracto de vainilla"]

cadena = "Hola me gustan los pasteles"

numeros= [4,8,12,16]

print("Necesitaras esto para un pastel")
indice = 1
# Estamos evitando una palabra especifica de la lista pero continuamos el blucle
for ingrediente in ingredientes_pastel:
    if ingrediente == "celular":
        continue
    print(f"Ingrediente número {indice} : {ingrediente}")
    indice += 1

# Evitamos que el bucle se siga ejecutando con la palabra break (El else que pertenece al for no se ejecutara)
for ingrediente in ingredientes_pastel:
    print(f"Ingrediente número: {indice}: {ingrediente}")
    indice += 1
    if ingrediente == "bicarbonato de sodio":
        break
else:
    print("terminado")

# Recorrer una cadena de texto (se hace caracter, por caracter)
for letra in cadena:
    print(letra)

# for en una linea
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)