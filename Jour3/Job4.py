from typing import List

class Joueur:
    def __init__(self, nom, numéro, position, nb_buts_marques, passes_décisives, cartons_jaunes, cartons_rouges):
        self.nom = nom
        self.numéro = numéro
        self.position = position
        self.nb_buts_marques = nb_buts_marques
        self.passes_décisives = passes_décisives
        self.cartons_jaunes = cartons_jaunes
        self.cartons_rouges = cartons_rouges

    def marquerUnBut(self):
        self.nb_buts_marques += 1

    def effectuerUnePasseDécisive(self):
        self.passes_décisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Nom : {self.nom}")
        print(f"Numéro : {self.numéro}")
        print(f"Position : {self.position}")
        print(f"Nombre de buts marqués : {self.nb_buts_marques}")
        print(f"Nombre de passes décisives : {self.passes_décisives}")
        print(f"Nombre de cartons jaunes : {self.cartons_jaunes}")
        print(f"Nombre de cartons rouges : {self.cartons_rouges}")

class Equipe:
    def __init__(self, nom, list_joueurs: List[Joueur] = []):
        self.nom = nom
        self.liste_joueurs = list_joueurs

    def ajouterJoueur(self, joueur):
           self.liste_joueurs.append(joueur)

    def AfficherStatistiquesJoueurs(self):
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDécisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()

# Création de joueurs
joueur1 = Joueur("Messi", 10, "Attaquant", 0, 0, 0, 0)
joueur2 = Joueur("Ronaldo", 7, "Attaquant", 0, 0, 0, 0)
joueur3 = Joueur("Modric", 8, "Milieu", 0, 0, 0, 0)

# Création d'une équipe
equipe = Equipe("Real Madrid")

# Ajout des joueurs à l'équipe
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)
equipe.ajouterJoueur(joueur3)

# Affichage des statistiques initiales des joueurs dans l'équipe
equipe.AfficherStatistiquesJoueurs()

print("----------")

# Mise à jour des statistiques d'un joueur
equipe.mettreAJourStatistiquesJoueur("Messi", "but")
equipe.mettreAJourStatistiquesJoueur("Ronaldo", "passe")
equipe.mettreAJourStatistiquesJoueur("Modric", "jaune")

# Affichage des statistiques mises à jour des joueurs dans l'équipe
equipe.AfficherStatistiquesJoueurs()
