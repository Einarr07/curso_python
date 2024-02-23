# Promedio de duraciones
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Duración de videos sin editar (crudos)
crudo_promedio = 5
crudo_dalto = 3.5

# Diferencias de duracion (A)
diferencia_con_min = 100 - (dalto_curso / otros_cursos_min * 100)
diferencia_con_max = 100 - (dalto_curso * 1000 // otros_cursos_max / 10)
diferencia_con_promedio = 100 - (dalto_curso / otros_cursos_promedio * 100)

# Calculamos el tiempo removido de los videos (B)
tiempo_vacio_promedio = 100 - (otros_cursos_promedio * 1000 // crudo_promedio / 10)
tiempo_vacio_dalto = 100 - (dalto_curso * 1000 // crudo_dalto / 10)

# Mostramos la diferencia de duración (ejercicio A)
print("EJERCICIO A")
print("El curso de dalto dura: ")
print(f"- Un {diferencia_con_min}% menos con el más rapido")
print(f"- Un {diferencia_con_max}% menos que el más lento")
print(f"- Un {diferencia_con_promedio}% menos que el promedio de los cursos")

# Mostramos la cantidad de espacio vacio, que se removio (ejercicio B)
print("\nEJERCICIO B")
print(f"Un curso promedio elimina {tiempo_vacio_promedio}% del video ")
print(f"Este curso elimino el {tiempo_vacio_dalto}% del video")

# Mostrando diferencia si los otros cursos duran 10h
print("\nEJERCICIO C")
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de "
      f"otros cursos")
print(f"Ver 10 horas de otros curso equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de "
      f"este cursos")