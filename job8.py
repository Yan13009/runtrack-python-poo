import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changer_rayon(self, new_rayon):
        self.rayon = new_rayon

    def afficher_infos(self):
        print(f"Informations du cercle - Rayon : {self.rayon}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return 2 * self.rayon


cercle1 = Cercle(rayon=4)
cercle2 = Cercle(rayon=7)


cercle1.afficher_infos()
print(f"Circonférence : {cercle1.circonference()}")
print(f"Diamètre : {cercle1.diametre()}")
print(f"Aire : {cercle1.aire()}")

cercle2.afficher_infos()
print(f"Circonférence : {cercle2.circonference()}")
print(f"Diamètre : {cercle2.diametre()}")
print(f"Aire : {cercle2.aire()}")
