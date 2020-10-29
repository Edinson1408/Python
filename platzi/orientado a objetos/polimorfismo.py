#modemos modificar los metodos que se heredan
#la habilidad de tomar varias formas
#por ejemplo sabemos que los vehiculos se desplazan , pero el carro se desplaza sobre ruedas el tren sobre rieles y el avion por aire
#como se los digo tenemos que capturar las abtraciones (abtraciones son lo que que hace el codigo pero no necesariamente esta expuesto o el usuario debe saber que hace exaactamente)

#en pocas palabras modificas el comportamiento de la super clase
#python nos permite cambiar el comporatamiento de una superclase para adaptarlo a la subclase

class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
    #esto se heredara en la parte de abajo
    def avanza(self):
        print('Ando Caminando')

class Ciclista(Persona):
    def __init__(self,nombre):
        #hereda avanza de al calse persona
        super().__init__(nombre)
    #modificamos las clase avanza , tiene que tener los mismos parametros
    #que la super clase
    def avanza(self):
        print('Ando pedaleando')
def main():
    persona=Persona('Davod')
    persona.avanza()
    ciclista=Ciclista('Daniel')
    ciclista.avanza()
if __name__=='__main__':
     main()
#puede usar el metodo heredado y normal y usando polimorfimos puedes cambiar
#el metodo heredado para que sevomporte segun lo quieres
    
