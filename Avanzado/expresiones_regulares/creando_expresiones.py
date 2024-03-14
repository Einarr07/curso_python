import re

# Creando un número CABA y ocultandolo

texto = "Hola Pedor, mi número es: +54 11 4521-1523"

patron = r"\+\d{2,3}\s\d{2}\s\d{4}-\d{4}"

remplazo = re.sub(patron, "Número oculto", texto)

print(remplazo)

