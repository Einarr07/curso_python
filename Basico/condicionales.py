# if-else
contrase_bd = 17
contrasenia_escrita = "123456"

if contrase_bd == contrasenia_escrita:
    print("Bienvenido")
else:
    print("Sus credenciales son incorrectas")

# else-if

ingreso_mensual = 1000

if ingreso_mensual > 100000:
    print("Estas bien economicamente en cualquier parte del mundo")
elif ingreso_mensual >= 1000:
    print("Estas bien economicamente en Latinoamerica")
else:
    print("Eres pobre")