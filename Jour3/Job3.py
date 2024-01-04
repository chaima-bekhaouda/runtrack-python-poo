class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_statut(self):
        return self.statut

    def set_statut(self, statut):
        self.statut = statut

class ListeDeTaches:
    def __init__(self, liste):
        self.titre = liste
        self.liste = []

    def ajouter_tache(self, tache: Tache):
        self.liste.append(tache)

    def supprimer_tache(self, tache: Tache):
        self.liste.remove(tache)

    def marquerCommeFinie(self,tache):
        tache.set_statut("finie")

    def afficher(self):
        print(f"Liste de tâches : {self.titre}")
        for tache in self.liste:
            print(f"Titre : {tache.titre}")
            print(f"Description : {tache.description}")
            print(f"Statut : {tache.statut}")
            print("----------")

    def filterList(self,filtrer):
        for tache in self.liste:
            if tache.statut == filtrer:
                print(f"Titre : {tache.titre}")
                print(f"Description : {tache.description}")
                print(f"Statut : {tache.statut}")
                print("----------")



# Création de quelques tâches
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes", "en cours")
tache2 = Tache("Faire le ménage", "Nettoyer la maison", "en cours")
tache3 = Tache("Faire du sport", "Aller courir", "en attente")

# Création d'une liste de tâches
liste_taches = ListeDeTaches("Liste principale")

# Ajout des tâches à la liste
liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)

# Affichage de la liste initiale de tâches
print("Liste initiale de tâches :")
liste_taches.afficher()

# Marquage d'une tâche comme "finie"
liste_taches.marquerCommeFinie(tache1)

# Affichage des tâches filtrées par statut "en cours"
print("Tâches en cours :")
liste_taches.filterList("en cours")

# Suppression d'une tâche de la liste
liste_taches.supprimer_tache(tache3)

# Affichage final de la liste mise à jour
print("Liste mise à jour de tâches :")
liste_taches.afficher()