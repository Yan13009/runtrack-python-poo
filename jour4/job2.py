class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=""):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'un Eleve
eleve1 = Eleve()
eleve1.bonjour()  # Fait dire bonjour à l'élève
eleve1.allerEnCours()  # Fait dire "Je vais en cours" à l'élève
eleve1.modifierAge(15)  # Redéfinit l'âge de l'élève à 15 ans
eleve1.afficherAge()  # Affiche le nouvel âge (15) en console

# Instanciation d'un Professeur
professeur2 = Professeur(age=40, matiereEnseignee="Physique")
professeur2.bonjour()  # Fait dire bonjour au professeur
professeur2.enseigner()  # Fait commencer le cours avec le professeur
