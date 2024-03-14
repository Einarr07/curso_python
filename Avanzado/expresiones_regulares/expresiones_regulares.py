import re

texto = """Hola joven, esta es la primera cadena de texto la 1
¿Cómo estas?, esta es la segunda linea osea la 2. 
numeros juntos 345
Y esta es la final la 3, chao."""

# Busqueda simple
# resultado = re.findall("Esta", texto)

# \d --> busca digitos númericos del 0 al 9
# resultado = re.findall(r"\d", texto)

# \D --> busca TODO menos digitos númericos
# resultado = re.findall(r"\D", texto)

# \w --> busca caracteres alfanumericos [a-z A-Z 0-9 _]
# resultado = re.findall(r"\w", texto)

# \W --> busca TODO menos caracteres alfanumericos
# resultado = re.findall(r"\W", texto)

# \s --> busca espacios en blanco -> espacios, tabs, saltos de linea
# resultado = re.findall(r"\s", texto)

# \S --> busca TODO menos espacios en blanco
# resultado = re.findall(r"\S", texto)

# \n --> busca saltos en linea
# resultado = re.findall(r"\n", texto)

# . --> busca TODO menos saltos en linea
# resultado = re.findall(r".", texto)


# \ --> cancelar caracteres especiales, cancelando la función del punto y buscando puntos
# busca puntos \. -- busca interogaciones \? ETC,ETC
# resultado = re.findall(r"\.", texto)

# Armando una cadena que busque un número, seguido de un punto y un espacio
# resultado = re.findall(r'\d\.\s', texto)

# ^ -> busca el comienzo de una linea (flags=re.M activa la multilinea)
# resultado = re.findall(r"^¿", texto, flags=re.M)

# $ -> busca el final de una linea
# resultado = re.findall(r".$", texto, flags=re.M)

# {n} -> busca n cantidad de veces el valor de la izquierda
# resultado = re.findall(r"\d{3}", texto)

# {n,m} -> almenos n, como máximo m
# resultado = re.findall(r"\d{1,4}", texto)

# | -> busca una cosa o la otra
resultado = re.findall(r"\d{1,4}|Hola", texto)

print(resultado)