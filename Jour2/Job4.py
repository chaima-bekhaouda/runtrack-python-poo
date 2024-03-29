class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits = 0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__student_eval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()
        else:
            print("Erreur: Le nombre de crédits doit être positif")

    def get_credits(self):
        return self.__credits

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prenom}")
        print(f"id = {self.__numero_etudiant}")
        print(f"Niveau = {self.__level}")


# Instanciation de l'étudiant John Doe
john_doe = Student("John", "Doe", 145)

# Ajout de crédits
john_doe.add_credits(15)
john_doe.add_credits(10)
john_doe.add_credits(5)

print(f"Le nombre de credits de John Doe est de {john_doe.get_credits()} points")

# Affichage des informations de l'étudiant
john_doe.student_info()