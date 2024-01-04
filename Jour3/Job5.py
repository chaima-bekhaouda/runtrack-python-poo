from random import choice

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
        self.defense = 0

    def attaquer(self, adversaire):
        adversaire.vie -= 10 + self.defense

    def se_defendre(self):
        self.defense += 5
        self.vie += 2

    def utiliser_objet_soin(self):
        self.vie += 20

    def esquiver(self):
        return choice([True, False])

class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None

    def choisirNiveau(self):
        self.niveau = int(input("\033[96mChoisissez le niveau de difficulté (1-3): \033[0m"))
        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 80
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 100
        else:
            vie_joueur = 60
            vie_ennemi = 120
        return vie_joueur, vie_ennemi

    def lancerJeu(self):
        vie_joueur, vie_ennemi = self.choisirNiveau()
        self.joueur = Personnage("\033[94mJoueur\033[0m", vie_joueur)
        self.ennemi = Personnage("\033[91mEnnemi\033[0m", vie_ennemi)

    def verifierSante(self, personnage):
        if personnage.vie <= 0:
            return False
        else:
            return True

    def verifierGagnant(self):
        if not self.verifierSante(self.joueur):
            return "\033[91mL'ennemi a gagné\033[0m"
        elif not self.verifierSante(self.ennemi):
            return "\033[92mLe joueur a gagné\033[0m"
        else:
            return "Le jeu continue"

# Exécution du jeu
jeu = Jeu()
jeu.lancerJeu()

while True:
    print(f"\nTour de jeu : {jeu.joueur.nom} vs {jeu.ennemi.nom}")

    print("\033[93mActions disponibles :\033[0m")
    print("1. \033[93mAttaquer\033[0m")
    print("2. \033[96mSe défendre\033[0m")
    print("3. \033[95mUtiliser un objet de soin\033[0m")
    print("4. \033[97mEsquiver\033[0m")

    choix_action = input("\033[93mChoisissez une action (1-4): \033[0m")

    if choix_action == '1':
        jeu.joueur.attaquer(jeu.ennemi)
        print(f"{jeu.joueur.nom} attaque {jeu.ennemi.nom} !")
    elif choix_action == '2':
        jeu.joueur.se_defendre()
        print(f"{jeu.joueur.nom} se défend et récupère de la vie.")
    elif choix_action == '3':
        jeu.joueur.utiliser_objet_soin()
        print(f"{jeu.joueur.nom} utilise un objet de soin.")
    elif choix_action == '4':
        esquive_reussie = jeu.joueur.esquiver()
        if esquive_reussie:
            print(f"{jeu.joueur.nom} esquive l'attaque de {jeu.ennemi.nom} !")
        else:
            jeu.ennemi.attaquer(jeu.joueur)
            print(f"{jeu.ennemi.nom} attaque {jeu.joueur.nom} !")
    else:
        print("\033[91mAction invalide. Veuillez choisir une action valide.\033[0m")

    ennemi_attaque = choice(['1', '2', '3', '4'])
    
    if ennemi_attaque == '1':
        jeu.ennemi.attaquer(jeu.joueur)
        print(f"{jeu.ennemi.nom} attaque {jeu.joueur.nom} !")
    elif ennemi_attaque == '2':
        jeu.ennemi.se_defendre()
        print(f"{jeu.ennemi.nom} se défend et récupère de la vie.")
    elif ennemi_attaque == '3':
        jeu.ennemi.utiliser_objet_soin()
        print(f"{jeu.ennemi.nom} utilise un objet de soin.")
    elif ennemi_attaque == '4':
        esquive_reussie = jeu.ennemi.esquiver()
        if esquive_reussie:
            print(f"{jeu.ennemi.nom} esquive l'attaque de {jeu.joueur.nom} !")
        else:
            jeu.joueur.attaquer(jeu.ennemi)
            print(f"{jeu.joueur.nom} attaque {jeu.ennemi.nom} !")

    print(f"{jeu.joueur.nom} : Vie = {jeu.joueur.vie}, {jeu.ennemi.nom} : Vie = {jeu.ennemi.vie}")

    resultat = jeu.verifierGagnant()
    print(resultat)

    if resultat != "Le jeu continue":
        break
