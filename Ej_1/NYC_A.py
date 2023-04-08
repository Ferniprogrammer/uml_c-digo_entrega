from clase_martín import Martin

class NYC_A(Martin):
    def __init__(self, nombre, edad, posicion, calle):
        super().__init__(nombre, edad, posicion)
        self.calle = calle
