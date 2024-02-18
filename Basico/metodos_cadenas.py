cadena1 = "Hola soy Mateo"

cadena2 = "¿Cómo estas?"

cadena3 = "5612313485"

cadena4 = "sadfsdjpjcxkcv"

# Es una función que devulve una lista de atributos válidos para el objeto pasado
dir()

# El metodo upper() convierte el texto en mayúsculas
mayusc = cadena1.upper()

# El metodo lower() convierte el texto en minúsculas
minisc = cadena1.lower()

# El metodo capitalize() convierte la primera en mayúscula
primer_letra_mayusc = cadena1.capitalize()

# El metodo find() busca un valor que le pidamos
# Cuando no encuentra un valor nos devuelve -1
busqueda_find = cadena1.find("y")

# El metodo index() busca un valor que le pidamos
# Cuando no encuentra nada nos da un error o una excepción
busqueda_index = cadena2.index("ó")

# El metodo isnumeric() verfica si el valor es numerico y devuelve true (Solo números)
es_numerico = cadena3.isnumeric()

# El metodo isalpha() verifica si es una letra / solo son validos las letras de la A a la Z (No puede contener espacios)
es_alfanumerico = cadena4.isalpha()

# El metodo count() devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("o")

# El metood len() devuelve la cantidad de caracteres que tiene una cadena
# Es una función
contar_caracteres = len(cadena1)

# El metodo startwith() verifica si una cadena empieza con contra cadena dada, si es así devuelve True
empieza_con = cadena1.startswith("H")

# El metodo endswith() verifica si una cadana termina con otra cadena dada, si es así devuelve True
termina_con = cadena3.endswith("5")

# El metodo replace() remplaza un pedado de cadana dada, por otro
# El valor 1 se debe encontrar en la cadena original para poder ser remplazado por el valor 2
remplazo = cadena2.replace("¿Cómo", "Cómo")

# El metodo split() separa cadenas con la cadena que le pasemos
cadena5 = "Hola,Juan,Te,Encuentras,Bien" # resultado: ['Hola', 'Juan', 'Te', 'Encuentras', 'Bien']
cadena_separada = cadena5.split(",")

print(cadena_separada[1])