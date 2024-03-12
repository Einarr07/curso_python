# Con el permiso "w" si no encuentra el arvhico lo crea
with open("mensaje.txt", "w" ,encoding="UTF-8") as archivo:
    # Sobre escribiendo el archivo
    # archivo.write("AJAJA, reescribi tu archivo, gil")

    # Agregando 2 lineas con writelines
    archivo.writelines(["Hola capo, ¿te trata bien la vida?\n", "¿Estas piola?\n"])

    # 2+
    archivo.writelines(["¿Viste la pelea del chito, el día sábado?\n", "Grande chito\n"])