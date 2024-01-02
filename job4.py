class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Addition de {self.nombre1} et {self.nombre2} : {resultat}")


operation_instance = Operation()


operation_instance.addition()
