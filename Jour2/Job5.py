class voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self):
        self.__annee

    def set_kilometrage(self):
        self.__kilometrage

    def set_en_marche(self):
        self.__en_marche

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture démarre")
        else:
            print("La voiture ne peut pas démarrer, le réservoir est trop bas.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")

    def __verifier_plein(self):
        return self.__reservoir > 5
