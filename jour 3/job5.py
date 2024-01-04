import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, cible):
        degats = random.randint(1, 10)
        cible.subir_degats(degats)
        print(f"{self.nom} attaque {cible.nom} et lui inflige {degats} points de dégâts.")

    def subir_degats(self, degats):
        self.vie -= degats
        if self.vie < 0:
            self.vie = 0

    def est_en_vie(self):
        return self.vie > 0


class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisir_niveau(self):
        try:
            self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))
            if self.niveau not in [1, 2, 3]:
                raise ValueError("Niveau invalide. Choisissez entre 1, 2 ou 3.")
        except ValueError as e:
            print(e)
            self.choisir_niveau()

    def lancer_jeu(self):
        self.choisir_niveau()

        if self.niveau == 1:
            vie_joueur = 50
            vie_ennemi = 30
        elif self.niveau == 2:
            vie_joueur = 40
            vie_ennemi = 40
        else:
            vie_joueur = 30
            vie_ennemi = 50

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        while joueur.est_en_vie() and ennemi.est_en_vie():
            joueur.attaquer(ennemi)
            if ennemi.est_en_vie():
                ennemi.attaquer(joueur)

        self.verifier_victoire(joueur, ennemi)

    def verifier_victoire(self, joueur, ennemi):
        if joueur.est_en_vie():
            print(f"{joueur.nom} a gagné !")
        else:
            print(f"{ennemi.nom} a gagné !")


# Exemple d'utilisation
jeu = Jeu()
jeu.lancer_jeu()
