class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe Operation
operation_instance = Operation()

# Impression en console des attributs "nombre1" et "nombre2"
print(f"Nombre 1: {operation_instance.nombre1}")
print(f"Nombre 2: {operation_instance.nombre2}")
