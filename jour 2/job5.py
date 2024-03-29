class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque
    
    def set_marque(self, marque):
        self.__marque = marque
    
    def get_modele(self):
        return self.__modele
    
    def set_modele(self, modele):
        self.__modele = modele
    
    def get_annee(self):
        return self.__annee
    
    def set_annee(self, annee):
        self.__annee = annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    
    def get_en_marche(self):
        return self.__en_marche
    
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche
    
    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Le réservoir est trop bas. La voiture ne peut pas démarrer.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")
    
    def __verifier_plein(self):
        return self.__reservoir > 5

# Exemple d'utilisation :
voiture = Voiture("Toyota", "Camry", 2020, 50000)
print(voiture.get_en_marche())  # Output: False

voiture.demarrer()               # Output: La voiture démarre.
print(voiture.get_en_marche())  # Output: True

voiture.arreter()                # Output: La voiture s'arrête.
print(voiture.get_en_marche())  # Output: False
