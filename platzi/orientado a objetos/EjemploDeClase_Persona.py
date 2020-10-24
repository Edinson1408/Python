#Deginicion
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def saluda(self,otra_persona):
        return f'Hola {otra_persona.nombre} , me llamo {self.nombre} y tengo {self.edad} años'

#uso 
Edinson=Persona('Edinson',25)
Rosa=Persona('Rosa',26)

print(Edinson.saluda(Rosa))
print(Rosa.saluda(Edinson))
