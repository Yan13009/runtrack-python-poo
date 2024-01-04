class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquer_un_but(self):
        self.buts_marques += 1

    def effectuer_une_passe_decisive(self):
        self.passes_decisives += 1

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1

    def afficher_statistiques(self):
        print(f"Statistiques de {self.nom} (#{self.numero}), {self.position}:")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")
        print()


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouter_joueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficher_statistiques()

    def mettre_a_jour_statistiques_joueur(self, numero, buts=0, passes=0, jaunes=0, rouges=0):
        for joueur in self.liste_joueurs:
            if joueur.numero == numero:
                joueur.buts_marques += buts
                joueur.passes_decisives += passes
                joueur.cartons_jaunes += jaunes
                joueur.cartons_rouges += rouges
                break


# Création des joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Modric", 8, "Milieu")
joueur4 = Joueur("Varane", 5, "Défenseur")

# Création des équipes
equipe1 = Equipe("Barcelone")
equipe2 = Equipe("Real Madrid")

# Ajout des joueurs aux équipes
equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur3)

equipe2.ajouter_joueur(joueur2)
equipe2.ajouter_joueur(joueur4)

# Affichage des statistiques initiales des joueurs
equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()

# Simulation d'un match avec des actions
joueur1.marquer_un_but()
joueur2.effectuer_une_passe_decisive()
joueur3.recevoir_un_carton_jaune()
joueur4.recevoir_un_carton_rouge()

# Mise à jour des statistiques des joueurs
equipe1.mettre_a_jour_statistiques_joueur(10, buts=1)
equipe2.mettre_a_jour_statistiques_joueur(7, passes=1)
equipe1.mettre_a_jour_statistiques_joueur(8, jaunes=1)
equipe2.mettre_a_jour_statistiques_joueur(5, rouges=1)

# Affichage des statistiques mises à jour des joueurs
equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()
