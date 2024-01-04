class Ville:
    def __init__(self, nom, nb_habitants):
      self.nom = nom
      self.nb_habitants = nb_habitants

    def getNom(self):
        return self.nom

    def getNb_habitants(self):
        return self.nb_habitants

    def ajouter_habitant(self):
        self.nb_habitants += 1

class Personne:
    def __init__(self, nom, age, ville: Ville):
        self.nom = nom
        self.age = age
        self.ville = ville
        self.ville.ajouter_habitant()

    def ajouterPopulation(self):
        self.ville.ajouter_habitant()

ville_Paris = Ville("Paris", 1000000)
print(f"Population de la ville de {ville_Paris.getNom()}: {ville_Paris.getNb_habitants()} habitants")

ville_Marseille = Ville("Marseille", 861635)
print(f"Population de la ville de {ville_Marseille.getNom()}: {ville_Marseille.getNb_habitants()} habitants")

John = Personne("John", 45, ville_Paris)
Myrtille = Personne("Myrtille", 4, ville_Paris)
Chloé = Personne("Chloé", 18, ville_Marseille)

print(f"Mise a jour de la population dela ville de {ville_Paris.getNom()}: {ville_Paris.getNb_habitants()} habitants")
print(f"Mise a jour de la population dela ville de {ville_Marseille.getNom()}: {ville_Marseille.getNb_habitants()} habitants")
