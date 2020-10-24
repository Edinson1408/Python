#parte en proble en porblemans mas pequeños
#las clase periten drear matores abstrancciones en for ade compomentes
#cada clase se encarga de una parte del problema y el progama se vuelve mas facil de matener 

#aqui hemos descompuesto los compomentes y puede utlizarse en automovil , 
class Automovil:
#self referencia de la intancia
    def __init__(self,modelo,marca,color ):
        self.modelo=modelo
        self.marca=marca
        self.color=color
        self._estado='en_reposo' #variable privada
        self._motor=Motor(cilindro=4)
    
    def acelerar(self,tipo='despacio'):
        if tipo=='rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(4)
        
        self._estado='en_movimiento'
    
class Motor:
    def __init__(self,cilindro,tipo='gasolina'): #parametro por defecto o defau kewor
        self.cilindro=cilindro
        self.tipo=tipo
        self._temperatura=0
    
    def inyecta_gasolina(self,cantidad): #metodo de la clase
        pass

        