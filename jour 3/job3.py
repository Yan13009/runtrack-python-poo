class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquer_comme_finie(self):
        self.statut = "Terminée"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
            print(f"Tâche '{tache.titre}' supprimée.")
        else:
            print("La tâche n'est pas présente dans la liste.")

    def marquer_comme_finie(self, tache):
        if tache in self.taches:
            tache.marquer_comme_finie()
            print(f"Tâche '{tache.titre}' marquée comme terminée.")
        else:
            print("La tâche n'est pas présente dans la liste.")

    def afficher_liste(self):
        print("Liste des tâches:")
        for tache in self.taches:
            print(f"{tache.titre} - {tache.statut}")

    def filter_liste(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list


# Exemples d'utilisation
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Chapitres 1 à 5")
tache3 = Tache("Faire du sport", "30 minutes de jogging")

liste_taches = ListeDeTaches()

liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)

liste_taches.afficher_liste()

tache4 = Tache("Rendre le devoir", "Avant la fin de la semaine")
liste_taches.ajouter_tache(tache4)

liste_taches.afficher_liste()

liste_taches.marquer_comme_finie(tache2)

liste_taches.afficher_liste()

liste_taches.supprimer_tache(tache1)

liste_taches.afficher_liste()

taches_a_faire = liste_taches.filter_liste("À faire")
print("Tâches à faire:")
for tache in taches_a_faire:
    print(tache.titre)
