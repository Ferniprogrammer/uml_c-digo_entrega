from clase_xing import Xing
class LA(Xing):
    def __init__(self, nombre, edad, posicion, calle):
        super().__init__(nombre, edad, posicion)
        self.calle = calle
