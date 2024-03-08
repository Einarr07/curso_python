# Utilizamos el parametro * como argumento *args (Debe ser el ultimo parametro que le pasemos)
def suma(nombre, *numeros):
    return f"Hola {nombre}, el resultado de tu suma es: {sum(numeros)}"


resultado = suma("Marco", 4,3,6,2,6,7)
print(resultado)

# No necesita ser el utlmo
def suma_total(numeros, nombre):
    return f"Hola {nombre}, la suma de tus numeros es: {sum([*numeros])}"

resultado2 = suma_total([78,98,5,93,8], "Matias")
print(resultado2)