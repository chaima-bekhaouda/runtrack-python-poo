class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHt = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * ( 1 + self.TVA / 100)

    def afficher(self):
        print(f"Le produit {self.getName()} coûte {self.getPriceTTC()} € TTC (TVA: {self.getTVA()}%)")

    def setName(self, newName):
        self.nom = newName

    def setPrice(self, newPrice):
        self.prixHT = newPrice

    def getName(self):
        return self.nom

    def getPriceTTC(self):
        return self.CalculerPrixTTC()

    def getPriceHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

produit1 = Produit("Telephone", 800, 30)
produit1.setName("SmartPhone")
produit1.setPrice(1000)
produit1.afficher()

produit2 = Produit("ordinateur", 1000, 30)
produit2.setName("Computer")
produit2.setPrice(800)
produit2.afficher()


produit3 = Produit("ecran", 200, 30)
produit3.setName("Screen")
produit3.setPrice(250)
produit3.afficher()


produit4 = Produit("clavier", 50, 30)
produit4.setName("Keyboard")
produit4.setPrice(70)
produit4.afficher()
