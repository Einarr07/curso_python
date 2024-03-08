# Creando una función simple
def saludar():
    print("Hola que tal?")


# Ejecutando una función simple
# saludar()

# Crear una función que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "maquina"
    else:
        adjetivo = "amor"

    print(f"Hola {nombre}, mi {adjetivo}, ¿cómo estas?")


saludar("Camila", "mujer")
saludar("Mateo", "HomBre")
saludar("Pepe", "idk")


# Crear una función que nos retorne valores
def crear_contraseña(num):
    caracteres = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{caracteres[c1]}{caracteres[c2]}{caracteres[c3]}{num * 2}"
    return contraseña, num


# Desempaquetando la función
contraseña, primer_numero = crear_contraseña(8)

# Mostramos los resultados y los datos utilizados para crear
print(f"Tu contraseña es: {contraseña}")
print(f"El número que utilizamos para crearlo fue: {primer_numero}")
