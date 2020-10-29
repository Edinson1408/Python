#enfocar en la informacion relevante
#separa la infomracion central de los detalles secundarios
#cuando menejas el automivil no te preocupas que hace el motor a detalle , sino solo te preocupas por mamejar
#es como usar una libreria solo nos interesa como interactuamos con la libreria 

class Lavadora:
    def __init__(self):
        pass
    def lavar(self,temperatura='caliente'):
        #metodos privados _
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()
#declarando los metos privados (_)
    def _llenar_tanque_de_agua(self,temperatura):
        print(f'Llenando el tanque con agua {temperatura}')
    def _añadir_jabon(self):
        print(f'Añadiendo jabon')
    def _lavar(self):
        print(f'Lavando la ropa')
    def _centrifugar(self):
        print(f'Centrifugando')

if __name__ == '__main__':
    lavadora=Lavadora()
    lavadora.lavar();


