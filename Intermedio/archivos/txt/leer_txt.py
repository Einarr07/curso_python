# Usando open para abrir un archivo con una codificación universal (UTF-8)
archivo_sin_leer = open("mensaje.txt", encoding="UTF-8")

# Leer archivo completo
# archivo = archivo_sin_leer.read()

# Leer linea por linea
# linea_1 = archivo_sin_leer.readlines()

# Leer una sola linea
linea = archivo_sin_leer.readline()

# Cerrar el archivo
archivo_sin_leer.close()

print(linea)