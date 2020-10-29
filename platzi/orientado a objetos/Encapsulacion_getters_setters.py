#permite agrupar datos ys u comportamiento 
#es como seguridad por que nos prmite controlar las modificaciones 
#tambien es aplicada  la programacion defensiva,para saver cuando y como se 
#mofica una calase
#controla el acceso a dicho datos
#previene modificaciones no autorizadas
#decoradores se definesn con el simbolo @


# Getter: Se encargará de interceptar la lectura del atributo. (get = obtener)

# Setter : Se encarga de interceptar cuando se escriba. (set = definir o escribir)

# Deleter : Se encarga de interceptar cuando es borrado. (delete = borrar)

# doc :  Recibirá una cadena para documentar el atributo. (doc = documentación)


class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None 
    #el siguente decorador nos permite modificcar la proiedad
    #de la region definida en la funcion
    @property
    def region(self):
        return self._region
    #el siguiente decorador es para setear lo que desea obtener
    #sin esto no podremo utilizar lo que region nos brinda 
    #(lo que se lleno previamente)
    
    @region.setter
    def region(self,region):
        if region in self._pais:
            self._region=region
        else :
            raise ValueError(f'La region {region} no es valido en el {self._pais}')

casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
print(casilla.region)
casilla.region = 'Mexico'
print(casilla.region)