class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    # Assesseurs
    def get_longueur(self):
        return self._longueur

    def get_largeur(self):
        return self._largeur

    # Mutateurs
    def set_longueur(self, longueur):
        self._longueur = longueur

    def set_largeur(self, largeur):
        self._largeur = largeur

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)

    def surface(self):
        return self._longueur * self._largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur

    # Assesseur
    def get_hauteur(self):
        return self._hauteur

    # Mutateur
    def set_hauteur(self, hauteur):
        self._hauteur = hauteur

    def volume(self):
        return self._longueur * self._largeur * self._hauteur


# Instanciation de la classe Rectangle
rectangle1 = Rectangle(longueur=5, largeur=3)

# Utilisation des méthodes et affichage des résultats
print("Rectangle:")
print(f"Longueur: {rectangle1.get_longueur()}")
print(f"Largeur: {rectangle1.get_largeur()}")
print(f"Périmètre: {rectangle1.perimetre()}")
print(f"Surface: {rectangle1.surface()}")

# Modification des attributs avec les mutateurs
rectangle1.set_longueur(8)
rectangle1.set_largeur(4)

# Affichage des résultats après modification
print("\nRectangle après modification:")
print(f"Longueur: {rectangle1.get_longueur()}")
print(f"Largeur: {rectangle1.get_largeur()}")
print(f"Périmètre: {rectangle1.perimetre()}")
print(f"Surface: {rectangle1.surface()}")

# Instanciation de la classe Parallelepipede
parallelepipede1 = Parallelepipede(longueur=3, largeur=2, hauteur=6)

# Utilisation des méthodes et affichage des résultats
print("\nParallélépipède:")
print(f"Longueur: {parallelepipede1.get_longueur()}")
print(f"Largeur: {parallelepipede1.get_largeur()}")
print(f"Hauteur: {parallelepipede1.get_hauteur()}")
print(f"Périmètre: {parallelepipede1.perimetre()}")
print(f"Surface: {parallelepipede1.surface()}")
print(f"Volume: {parallelepipede1.volume()}")
