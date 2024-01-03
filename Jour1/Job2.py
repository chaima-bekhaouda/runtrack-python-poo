class Operation:
    def __init__(self,nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation_obj = Operation(12, 3)

print(f"Le nombre1 est", operation_obj.nombre1)
print(f"Le nombre2 est", operation_obj.nombre2)