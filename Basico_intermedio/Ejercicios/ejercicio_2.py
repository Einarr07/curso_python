# Crear una función que genere números primos hasta llegar al numero que le pasamos.

# Creamos una función que verifique si un número es primo
def es_primo(num):
    # Verificamos que el número pasado no pueda dividirse
    # por ningun número entre 2 y ese mismo número -1
    for i in range(2, num-1):
        # Si es divisible por alguno retornamos false y termina el bucle
        if num%i == 0:
            return False
    # Si termina el bucle, significa que no fue divisible entonces es primo
    return True


# Creamos una función que retorne una lista con todos los números primos
def primos_hasta(num):
    # Creamos la lista
    primos = []
    for i in range(2, num+1):
        # Verificamos si el valor es primo
        resultado = es_primo(i)
        # En caso de que sea lo agregamos a la lista
        if resultado == True:
            primos.append(i)
    # Devolvemos la lista
    return primos


# Creamos el resultado llamando a la función y lo mostramos
num = int(input("Ingresa un número para saber cuales son todos los números primos anterirores a el: "))
resultado = primos_hasta(num)
print(f"La lista de números primos es: \n{resultado}")