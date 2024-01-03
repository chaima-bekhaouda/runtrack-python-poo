class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Le point a pour coordonnées ({self.x}, {self.y})")

    def afficherX(self):
        print(self.x)

    def afficherY(self):
        print(self.y)

    def changerX(self, nouvelle_valeur_de_x):
        self.x = nouvelle_valeur_de_x

    def changerY(self, nouvelle_valeur_de_y):
        self.y = nouvelle_valeur_de_y
