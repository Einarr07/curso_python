with open("mensaje.txt", "a" ,encoding="UTF-8") as archivo:
    # Usando un bucle para agregar varias lineas
    archivo.write("\n")
    for i in range(5):
        # Agregando lineas
        archivo.write(f"Linea {i+1} agg\n")

