class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"
    
    def ajouter_plat(self, nom_plat, prix, statut="en cours"):
        self.__plats_commandes[nom_plat] = {"prix": prix, "statut": statut}
    
    def annuler_commande(self):
        self.__statut_commande = "annulée"
    
    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values() if plat["statut"] == "en cours")
        return total
    
    def afficher_commande(self):
        total = self.__calculer_total()
        print(f"Commande #{self.__numero_commande}")
        for plat, details in self.__plats_commandes.items():
            print(f"{plat}: {details['prix']} $ - Statut: {details['statut']}")
        print(f"Total à payer: {total} $")
    
    def calculer_tva(self):
        total = self.__calculer_total()
        tva = total * 0.1  
        return tva


commande1 = Commande(1)


commande1.ajouter_plat("Pizza", 15)
commande1.ajouter_plat("Burger", 10, "terminé")


commande1.afficher_commande()


commande1.annuler_commande()
commande1.afficher_commande()  


tva = commande1.calculer_tva()
print(f"TVA à payer: {tva} $")
