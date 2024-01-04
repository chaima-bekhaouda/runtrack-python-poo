class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {'prix': prix_plat, 'statut': 'non livré'}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print(f"Le plat '{nom_plat}' est déjà dans la commande.")

    def annuler_commande(self):
        self.__plats_commandes = {}
        self.__statut_commande = "annulée"
        print("La commande a été annulée.")

    def __calculer_total(self):
        total = sum(plat['prix'] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande}:")
        for plat, details in self.__plats_commandes.items():
            print(f"- {plat}: {details['prix']}€ ({details['statut']})")
        total = self.__calculer_total()
        print(f"Total à payer : {total}€")

    def calculer_tva(self, taux_tva):
        total = self.__calculer_total()
        tva = total * (taux_tva / 100)
        return tva

# Test de la classe Commande
if __name__ == "__main__":
    ma_commande = Commande(123)
    ma_commande.ajouter_plat("Pizza", 10)
    ma_commande.ajouter_plat("Salade", 5)
    ma_commande.ajouter_plat("Pizza", 10)
    ma_commande.afficher_commande()
    ma_commande.annuler_commande()
    ma_commande.afficher_commande()

    tva = ma_commande.calculer_tva(20)
    print(f"TVA à payer : {tva}€")
