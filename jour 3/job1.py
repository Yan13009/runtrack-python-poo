class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def ajouter_population(self):
        self.__nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        ville.ajouter_population()

    def ajouterPopulation(self):
        self.__ville.ajouter_population()


# Création d'un objet Ville avec comme arguments “Paris” et 1000000.
paris = Ville("Paris", 1000000)

# Affichage du nombre d’habitants de la ville de Paris.
print(f"Nombre d'habitants à {paris.get_nombre_habitants()} Paris")

# Création d'un autre objet Ville avec comme arguments “Marseille” et 861635.
marseille = Ville("Marseille", 861635)

# Affichage du nombre d’habitants de la ville de Marseille.
print(f"Nombre d'habitants à Marseille : {marseille.get_nombre_habitants()}")

# Création des objets demandés.
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage du nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.
print(f"Nombre d'habitants à Paris après l'arrivée de nouvelles personnes : {paris.get_nombre_habitants()}")
print(f"Nombre d'habitants à Marseille après l'arrivée de nouvelles personnes : {marseille.get_nombre_habitants()}")
