# Creando una función que suma numeros
def sumar_dos():
    # Iniciando el bucle
    while True:
        a = input("Ingresa el primer número: ")
        b = input("Ingresa el segundo número: ")
        # Convertimos a enteros y lo sumamos
        try:
            resultado = int(a) + int(b)
        # Si lanzo una excepción, pedirle al usuario que ingrese bien los datos
        except Exception as e:
            print("Te pedí un número, no te hagas el gracioso")
            print(f"ERROR: {e}")
        # Si todo salio ok terminamos el bucle
        else:
            break
        # Esto se ejecuta siempre
        finally:
            print("Esto se ejecuta siempre")

    # Mostrando el resultado
    return print(f"El resultado es: {resultado}")

sumar_dos()