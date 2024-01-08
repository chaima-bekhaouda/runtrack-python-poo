# Définition de la classe Personne
class Personne:
    def __init__(self, age=14):  # Initialisation de la classe Personne avec un âge par défaut de 14 ans
        self._age = age  # Attribution de l'âge à l'attribut protégé _age

    def afficherAge(self):  # Méthode pour afficher l'âge de la personne
        print(f"L'âge de la personne est de {self._age} ans")

    def bonjour(self):  # Méthode pour dire bonjour
        print("Hello!")

    def modifierAge(self, nouvel_age):  # Méthode pour modifier l'âge de la personne
        self._age = nouvel_age

# Définition de la classe Eleve qui hérite de la classe Personne
class Eleve(Personne):
    def allerEnCours(self):  # Méthode pour indiquer que l'élève va en cours
        print("Je vais en cours")

    def afficherAge(self):  # Méthode pour afficher l'âge spécifique de l'élève
        print(f"J'ai {self._age} ans")

# Définition de la classe Professeur qui hérite de la classe Personne
class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):  # Initialisation de la classe Professeur avec l'âge et la matière enseignée
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee  # Attribution de la matière enseignée à l'attribut privé __matiereEnseignee

    def enseigner(self):  # Méthode pour indiquer que le professeur commence le cours
        print("Le cours va commencer")

# Instanciation d'une classe Personne et Eleve
personne = Personne()  # Création d'une personne avec l'âge par défaut
eleve = Eleve()  # Création d'un élève

# Affichage de l'âge par défaut de l'élève
eleve.afficherAge()

# Modification de l'âge de l'élève à 15 ans
eleve.modifierAge(15)

# Appels des méthodes pour l'élève et le professeur
eleve.bonjour()  # Dire bonjour en tant qu'élève
eleve.allerEnCours()  # Indiquer que l'élève va en cours

# Instanciation d'un objet Professeur
professeur = Professeur(age=40, matiereEnseignee="Mathématiques")  # Création d'un professeur de 40 ans enseignant les mathématiques

professeur.bonjour()  # Dire bonjour en tant que professeur
professeur.enseigner()  # Indiquer que le cours commence
