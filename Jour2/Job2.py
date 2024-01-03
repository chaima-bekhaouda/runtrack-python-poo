class Livre:
    def __init__(self, titre, auteur, n_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__n_pages = n_pages

    def getTitre(self):
        return self.__tittre

    def getAuteur(self):
       return self.__auteur

    def getN_pages(self):
        return self.__n_pages

    def setTitre(self, titre):
        self.__titre = titre

    def setAuteur(self, auteur):
        self.__auteur = auteur

    def setN_pages(self, n_pages):
        if n_pages > 0:
            self.__n_pages = n_pages
        else:
            print("Erreur: Le nombre de pages doit être positif")