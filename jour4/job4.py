class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

# Instanciation de la classe Rectangle
rectangle1 = Rectangle(largeur=5, hauteur=3)

# Appel de la méthode aire de la classe Rectangle
resultat_aire_rectangle = rectangle1.aire()

# Affichage du résultat en console
print(f"L'aire du rectangle est : {resultat_aire_rectangle}")
