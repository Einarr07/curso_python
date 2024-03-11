# Creando una función que muestre la serie fibonacci entre 0 al número dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num:
            return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b = b, a+b


numero = int(input("Ingresa un número para crear la serie fibonacci: "))

resultado = fibonacci(numero)

print(f"La serie de fibonacci del número {numero} es: \n{resultado}")