class Livre:
    def __init__(self, titre, auteur, n_pages, disponible = True):
        self.__titre = titre
        self.__auteur = auteur
        self.__n_pages = n_pages
        self.__disponible = disponible

    def getTitre(self):
        return self.__titre

    def getAuteur(self):
       return self.__auteur

    def getN_pages(self):
        return self.__n_pages

    def getDisponible(self):
        return self.__disponible

    def setTitre(self, titre):
        self.__titre = titre

    def setAuteur(self, auteur):
        self.__auteur = auteur

    def setN_pages(self, n_pages):
        if n_pages >= 0:
            self.__n_pages = n_pages
        else:
            print("Erreur: Le nombre de pages doit être positif")

    def setDisponible(self, disponible):
        self.__disponible = disponible

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else:
            print("Erreur: Le livre n'est pas disponible")

    def rendre(self):
        if self.verification():
            print("Erreur: Le livre est déjà disponible")
        else:
            self.__disponible = True