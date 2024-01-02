class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}"

# Instanciation de la classe Personne
personne1 = Personne(nom="Doe", prenom="John")
personne2 = Personne(nom="Smith", prenom="Alice")

# Appel de la méthode se_presenter
print(personne1.se_presenter())
print(personne2.se_presenter())
