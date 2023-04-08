from NYC_A import NYC_A
from NYC_B import NYC_B
class NYC(NYC_A, NYC_B):
    def __init__(self, nombre, edad, posicion, calle):
        super().__init__(nombre, edad, posicion, calle)
