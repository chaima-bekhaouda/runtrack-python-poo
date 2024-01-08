class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Année : {self.annee}")
        print(f"Prix : {self.prix}")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes : {self.portes}")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roues}")


# Instanciation de l'objet Voiture
voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
voiture.informationsVehicule()

# Instanciation de l'objet Moto
moto = Moto("Honda", "CBR500R", 2021, 7500)
moto.informationsVehicule()
