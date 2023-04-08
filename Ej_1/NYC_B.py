from clase_salim import Salim
class NYC_B(Salim):
    def __init__(self, nombre, edad, posicion, calle):
        super().__init__(nombre, edad, posicion)
        self.calle = calle
