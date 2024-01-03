class animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

animal_obj = animal()
print(f"L'age de l'animal {animal_obj.age} ans")

animal_obj.vieillir()
print(f"L'age de l'animal {animal_obj.age} ans")

animal_obj.nommer("Luna")
print(f"L'animal se nomme {animal_obj.prenom}")
