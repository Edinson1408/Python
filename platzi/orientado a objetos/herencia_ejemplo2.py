class Area:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def calcular_area(self):
        return self.base*self.altura

class Rectangulo(Area):
    def __init__(self,base,altura):
        super().__init__(base,altura)

class Cuadrado(Area):
    def __init__(self,lado):
        super().__init__(lado,lado)

rectangulo=Rectangulo(base=3,altura=4)
print(rectangulo.calcular_area())

cuadrado=Cuadrado(lado=5)
print(cuadrado.calcular_area())