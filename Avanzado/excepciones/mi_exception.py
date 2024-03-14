# Creando mi propia excepción personalizada
class MiException(Exception):
    def __init__(self,err):
        print(f"Cometiste el siguente error: {err}")


# Lanzando mi propia excepción
# raise MiException("gil")

# Manejando mi propia excepción
try:
    raise MiException("jaja, persona poco culta")
except:
    print("Como vas a cometer ese error?")