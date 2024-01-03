class Operation:
    def __init__(self, nombre1, nombre2):
       self.nombre1 = nombre1
       self.nombre2 = nombre2


    def addition(self):
        return self.nombre1 + self.nombre2

operation_obj = Operation(12, 3)
print("resultat de l'addition:", operation_obj.addition())