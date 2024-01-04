class CompteBancaire:
    def __init__(self, nm_compte, nom, prenom, solde, decouvert: bool = False):
        self.__nm_compte = nm_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        droit_decouvert = "Oui" if self.__decouvert else "Non"
        affichage = (
            f"Numéro de compte : {self.__nm_compte}\n"
            f"Nom du titulaire : {self.__nom}\n"
            f"Prénom du titulaire : {self.__prenom}\n"
            f"Solde du compte : {self.__solde} €\n"
            f"Droit au découvert : {droit_decouvert}"
        )
        print(affichage)

    def afficherSolde(self):
        print(f"Solde du compte {self.__nm_compte} : {self.__solde} €")

    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant} € effectué avec succès sur le compte {self.__nm_compte}.")
        else:
            print("Le montant du versement doit être positif.")

    def retrait(self, montant):
        if montant > 0 or (self.__decouvert and montant <= -self.__solde):
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué avec succès sur le compte {self.__nm_compte}.")
        else:
            print(f"Opération impossible. Vérifiez le montant du retrait sur le compte {self.__nm_compte}.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Des agios de {agios} € ont été appliqués au solde du compte {self.__nm_compte}.")

    def virement(self, beneficiaire, montant):
        if montant > 0 and montant <= self.__solde:
            self.__solde -= montant
            beneficiaire.versement(montant)
            print(f"Virement de {montant} € effectué avec succès du compte {self.__nm_compte} vers le compte {beneficiaire.__nm_compte}.")
        else:
            print(f"Opération de virement impossible. Vérifiez le montant du virement sur le compte {self.__nm_compte}.")

# Exemple d'utilisation
compte1 = CompteBancaire("12345", "Doe", "John", 1000)
compte1.afficher()
print("----------")

compte2 = CompteBancaire("54321", "Smith", "Alice", -200, decouvert=True)
compte2.afficher()
print("----------")

compte1.versement(500)
compte1.afficherSolde()
print("----------")

compte1.retrait(200)
compte1.afficherSolde()
print("----------")

compte1.afficherSolde()
print("----------")

compte2.afficherSolde()
compte2.agios(0.05)
compte2.afficherSolde()
print("----------")

compte1.agios(0.05)
compte1.virement(compte2, 210)
print("----------")

compte1.afficherSolde()
compte2.afficherSolde()
