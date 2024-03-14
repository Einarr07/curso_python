# 2 listas, una con nombres otra con apellidos
nombres = ["Martin", "Dylan", "Felipe","Camila","Melanie"]
apellidos = ["Folleco","Espinosa","Mier","Ortiz","Cedeño"]

# Registrar los datos en un txt de forma optima
with open("nombres_apellidos.txt", "w", encoding="UTF-8") as txt:
    txt.writelines("Los datos son:\n \n")
    [txt.writelines(f"Nombre: {n}\nApellido: {a}\n-------------\n") for n,a in zip(nombres, apellidos)]