# Tener esto :
multiplicar_por_dos = lambda x: x * 2  # Creando una función lambda para multiplicar por dos


# Es igual a tener esto:
def por_dos(x):
    return x * 2


print(f"El resultado de la función LAMBDA es: {multiplicar_por_dos(7)}")

resultado = por_dos(7)
print(f"El resultado de la función es: {resultado}")

# Creando una lista de números
numeros = [1,2,3,4,5,6,7,8,9,10]

# Función lambda
numeros_pares = filter(lambda num:num%2 == 0, numeros)
print(list(numeros_pares))

# Función normal
def es_par(num):
    if num%2 == 0:
        return True

si_es_par = filter(es_par,numeros)
print(si_es_par)