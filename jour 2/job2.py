class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
    
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

# Exemple d'utilisation :
livre = Livre("Titre1", "Auteur1", 200)
print(livre.get_titre())          # Output: Titre1
print(livre.get_auteur())         # Output: Auteur1
print(livre.get_nombre_pages())   # Output: 200

livre.set_nombre_pages(300)
print(livre.get_nombre_pages())   # Output: 300

livre.set_nombre_pages(-50)       # Output: Erreur: Le nombre de pages doit être un nombre entier positif.
