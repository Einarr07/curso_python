# El usuario ingresa la frase
frase = input("Ingresa una frase y te calculare cuanto tiempo te tardarias en decirla : ")

# Utilizamos el metodo split() para separar la cadena por cada espació que se encuentre en ella
palabras_separadas = frase.split(" ")

# Contamos las palabras dichas
cantidad_de_palabras = len(palabras_separadas)

if cantidad_de_palabras > 120:
    print("OYE!!, tampoco te pedí un testamento")

# Contamos el número de palabras que existe dentro de nuestra lista
print(f"En tu frase dijiste: {cantidad_de_palabras} palabras, y te tomaria {cantidad_de_palabras/2} segundos "
      f"decirlas")

print(f"\nDalto tardaria en decir la misma frase en {cantidad_de_palabras/2*1.3} segundos")

