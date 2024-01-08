import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius ** 2

# Création d'une instance de Rectangle
mon_rectangle = Rectangle(5, 10)
# Affichage de l'aire du rectangle
print("Aire du rectangle:", mon_rectangle.aire())

# Création d'une instance de Cercle
mon_cercle = Cercle(7)  # Par exemple, un cercle avec un rayon de 7 unités
# Affichage de l'aire du cercle
print("Aire du cercle:", mon_cercle.aire())
