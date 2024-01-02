class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher_les_points(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficher_x(self):
        print(f"Coordonnée x : {self.x}")

    def afficher_y(self):
        print(f"Coordonnée y : {self.y}")

    def changer_x(self, new_x):
        self.x = new_x

    def changer_y(self, new_y):
        self.y = new_y

# Instanciation de la classe Point
point_instance = Point(x=3, y=5)

# Utilisation des méthodes
point_instance.afficher_les_points()
point_instance.afficher_x()
point_instance.afficher_y()

point_instance.changer_x(8)
point_instance.changer_y(10)

point_instance.afficher_les_points()
