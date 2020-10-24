#objetivos 
#enteder como funciona la programcion orienta a objetivos
# las clasees prveen las estructuras
#Las clases nos permiten crear nuevos tipos que contiene información arbitraria sobre un objeto.
# Atributos de la instancia
# Todas las clases crean objetos y todos los objetos tienen atributos. Utilizamos
# el método especial __init__ para definir el estado inicial de nuestra instancia.
# Recibe como primer parámetro obligatorio self (que es simplemente una
# referencia a la instancia).

#atributos comeinza con self (this)
class Hotel:
    
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0

#Métodos de instancia
class Hotel:

    pass

    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupacion_total(self):
        return self.huespedes


hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
hotel.checkout(1)
hotel.ocupacion_total() # 2

#tipos que se crean son los datoa abstractos listas variables .etc
#se pueden hacer 3 cosas eon los objetos creaciion, manipulacion y destruirlos
#ventajas:
#decomposicion:estructurar a ibjetos mas pequeños
#abtrancciones: solo lo que se necesita
#encapsulacion : esconder datos que no son importante ára las personas q utilizan nuestas clases o objetos


