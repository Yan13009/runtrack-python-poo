class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte n°{self.__numero_compte} - {self.__nom} {self.__prenom}")
        self.afficherSolde()

    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué.")
        self.afficherSolde()

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué.")
            self.afficherSolde()
        else:
            print("Solde insuffisant. Opération impossible.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Agios de {agios} € appliqués.")
            self.afficherSolde()

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero_compte}.")
            self.afficherSolde()
        else:
            print("Solde insuffisant. Opération impossible.")



compte_normal = CompteBancaire(numero_compte="12345", nom="Doe", prenom="John", solde=1000)
compte_normal.afficher()


compte_decouvert = CompteBancaire(numero_compte="67890", nom="Smith", prenom="Jane", solde=-500, decouvert=True)
compte_decouvert.afficher()


compte_normal.virement(compte_decouvert, 1500)
