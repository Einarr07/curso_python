# ANALOGIA PLAYA

# Creamos un conjunto con set()
conjunto = set(["Arena", "Sol"])

# Metemos un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Zapatillas", "Traje de baño"])
conjunto2 = {conjunto1, "Sombrilla"}

print(conjunto2)

# Teoria de conjuntos

# Verificamos si es un subconjunto
conjunto_teoria = {"Pelota de playa", "Jugo de coco", "Barcos", "Salva vidas"}
conjunto_teoria2 = {"Jugo de coco", "Salva vidas"}

resultado = conjunto_teoria2.issubset(conjunto_teoria)
print(f"El conjunto_teoria2 es un subconjunto de conjunto_teoria?: {resultado}")

# Verificamos si es un superconjunto
resultado_super = conjunto_teoria.issuperset(conjunto_teoria2)

# Verificamos si hay alguna palabra en comun
resultado = conjunto_teoria2.isdisjoint(conjunto_teoria)
print(resultado) # Cuando solo 1 elemento coincide ya deja de ser distinto