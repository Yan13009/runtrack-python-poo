class Animal:
    def __init__(self):
        self.age = 0
        self.nom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.nom = nom

# Instanciation de la classe Animal
animal_instance = Animal()

# Affichage initial de l'âge
print(f"Âge de l'animal : {animal_instance.age}")

# Vieillissement de l'animal
animal_instance.vieillir()
print(f"Âge de l'animal après vieillissement : {animal_instance.age}")

# Nommer l'animal
animal_instance.nommer("Fido")
print(f"Nom de l'animal : {animal_instance.nom}")
