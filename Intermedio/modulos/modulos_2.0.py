# Hacemos esto cuendo nuestra importación esta fuera de la carpeta que necesitamos.
# utilizamos el módulo sys para agregar la ruta donde se encuentra nuestro archivo
import sys
sys.path.append("C:\\Users\\ASUS\\PycharmProjects\\Cursos_de_programacion\\Intermedio\\import_modulos")

# Puede salir un error en saludar, pero podemos utilizarlo de todas formas
import saludar as modulo_saludo

print(modulo_saludo.saludar(input("¿Cuál es tu nombre: ")))

# Cuando el modulo esta dentro de una carpeta de la misma ruta
# import funcion_saludar.saludar as f_saludar

# print(f_saludar.saludar(input("Ingresa tu nombre: ")))