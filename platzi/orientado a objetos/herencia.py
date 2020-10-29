#permite modelas una jerarqui de las clases
#permite compartir comportamioent comun en la jerarquia
#la padre se lo comoce como super clase y al hijo como sub clase
#comparte coportamiento entre objetos , codigo ordenado y que la jerarquia tenga sentido


#ejemplo los animales puedes dividirse en herbivoros y carniboros
#quiiere decir que la superclase es animales y las subcalses son herviboros y carnivoros
#a parte los carnivoros son felinos o caninos ,
#aqui observamos que hay subclase de uan subcalse que tiene una superclase llamada animal 
#como uan especie de piramide que va por jerarquia de como lo engloba por caractericas

class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base*self.altura
    
class Cuadrado(Rectangulo):  #la clase cuadrado extiende al cuadrado
    def __init__(self,lado):
        #este super genera que heredemos los metodos del rectangulo
        #en cristiano ahora podemos calcular el area
        #enviamos lado , lado por que el area del cuadro es lado al cuadro
        #entonces lado * lado
        super().__init__(lado,lado) 


if __name__=='__main__':
    rectangulo=Rectangulo(base=3,altura=4)
    print(rectangulo.area())

#observamos que la clase cuadrado no tiene un meotodo de area
#pero lo hereda del rectangulo
    cuadrado=Cuadrado(lado=5)
    print(cuadrado.area())
