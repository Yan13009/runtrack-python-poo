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


# Instanciation d'une Personne
personne1 = Personne()
personne1.afficherAge()  # Affiche l'âge par défaut (14) en console
personne1.bonjour()  # Affiche "Hello" en console
personne1.modifierAge(25)  # Modifie l'âge de la personne à 25
personne1.afficherAge()  # Affiche le nouvel âge (25) en console

# Instanciation d'un Eleve
eleve1 = Eleve()
eleve1.afficherAge()  # Affiche l'âge par défaut (14) en console
eleve1.allerEnCours()  # Affiche "Je vais en cours" en console

# Instanciation d'un Professeur
professeur1 = Professeur(age=35, matiereEnseignee="Mathématiques")
professeur1.afficherAge()  # Affiche l'âge par défaut (35) en console
professeur1.enseigner()  # Affiche "Le cours va commencer" en console
