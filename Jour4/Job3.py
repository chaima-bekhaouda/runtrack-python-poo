class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # attribut longueur
        self.__largeur = largeur    # attribut largeur

    # Accesseurs pour la longueur et la largeur
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs pour la longueur et la largeur
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    # Méthode pour calculer le périmètre
    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2

    # Méthode pour calculer la surface
    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    # Méthode pour calculer le volume du parallélépipède
    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur

    # Méthode pour calculer la surface du parallélépipède
    def surface(self):
        return (self.get_longueur() * self.get_largeur() + self.get_longueur() * self.__hauteur + self.get_largeur() * self.__hauteur) * 2


# Instanciation d'un objet de type Rectangle
mon_rectangle = Rectangle(5, 10)

# Accès aux attributs et utilisation des méthodes
print("Longueur du rectangle:", mon_rectangle.get_longueur())
print("Largeur du rectangle:", mon_rectangle.get_largeur())

# Calcul du périmètre et de la surface
print("Périmètre du rectangle:", mon_rectangle.perimetre())
print("Surface du rectangle:", mon_rectangle.surface())
