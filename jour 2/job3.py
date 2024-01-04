
class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
    
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
    
    def get_nombre_pages(self):
        return self.__nombre_pages
    
    def set_nombre_pages(self, nombre_pages):
        if isinstance(nombre_pages, int) and nombre_pages > 0:
            self.__nombre_pages = nombre_pages
        else:
            print("Erreur: Le nombre de pages doit être un nombre entier positif.")
    
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible.")
    
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Le livre est déjà disponible.")

# Exemple d'utilisation :
livre = Livre("Titre1", "Auteur1", 200)
print(livre.verification())  # Output: True

livre.emprunter()            # Output: Livre emprunté avec succès.
livre.rendre()               # Output: Livre rendu avec succès.
