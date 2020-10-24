class Coordenada:
    def __init__ (self ,x, y ) : #construnctor
          self.x=x
          self.y=y
    def distancia(self,otra_coordenada):
        x_diff=(self.x-otra_coordenada.x)**2
        y_diff=(self.x-otra_coordenada.y)**2

        return (x_diff+y_diff)**0.5 #raiz cuadrada

if __name__ =='__main__':
    coorf_1=Coordenada(3,30)
    coorf_2=Coordenada(4,8)

    print(coorf_1.distancia(coorf_2))
    print(coorf_2.x)
    print(coorf_2.y)
    print(isinstance(coorf_2,Coordenada)) #la xoordebara coord2 es una instancia de coordenada 
    print(isinstance(3,Coordenada))

        