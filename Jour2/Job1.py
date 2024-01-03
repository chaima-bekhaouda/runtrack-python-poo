class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def getLongueur(self):
        return self.__longueur

    def getLargeur(self):
        return self.__largeur

    def setLongueur(self, longueur):
        self.__longueur = longueur

    def setLargeur(self, largeur):
        self.__largeur = largeur

rectangle_obj = Rectangle(10, 5)

print(f"Longueur avant = {rectangle_obj.getLongueur()}")
print(f"Largeur avant = {rectangle_obj.getLargeur()}")

rectangle_obj.setLongueur(5)
rectangle_obj.setLargeur(10)

print("----------")

print(f"Longueur après = {rectangle_obj.getLongueur()}")
print(f"Largeur après = {rectangle_obj.getLargeur()}")