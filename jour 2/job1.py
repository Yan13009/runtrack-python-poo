class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur


rectangle = Rectangle(10, 5)
print(rectangle.get_longueur())  # Output: 10
print(rectangle.get_largeur())   # Output: 5

rectangle.set_longueur(15)
rectangle.set_largeur(8)
print(rectangle.get_longueur())  # Output: 15
print(rectangle.get_largeur())   # Output: 8
