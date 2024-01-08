class Forme:
    def air(self):
        return 0

class Rectangle(Forme):
        def __init__(self, largeur, hauteur):
          self.largeur = largeur
          self.hauteur = hauteur

        def aire(self):
          return self.largeur * self.hauteur

# Création d'un objet de type Rectangle
mon_rectangle = Rectangle(5, 10)

# Affichage du résultat de la méthode aire de la classe Rectangle
print("Aire du rectangle:", mon_rectangle.aire())