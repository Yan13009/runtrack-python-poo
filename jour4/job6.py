class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Prix: {self.prix}")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")


# Instanciation d'une voiture et appel de la méthode informationsVehicule
voiture1 = Voiture(marque="Toyota", modele="Corolla", annee=2022, prix=25000)
voiture1.informationsVehicule()

# Affichage d'une ligne pour séparer les résultats
print("\n" + "=" * 40 + "\n")

# Instanciation d'une moto et appel de la méthode informationsVehicule
moto1 = Moto(marque="Harley-Davidson", modele="Sportster", annee=2021, prix=12000)
moto1.informationsVehicule()
