#metodos que se puede utilizar
nombre='edinson'


## string en mayusculas
print(nombre.upper())
## poner la primera letra en mayuscula
print(nombre.capitalize())
## ELiminar los espacio de un string
print(nombre.strip()) 
## poner en minuscula un string
print(nombre.lower())

## susutituir un string por otro
print(nombre.replace('e','a'))


## El nomnbre tambien es un objeto como un array
print(nombre[0])



## El String tambien se puede contar 
print(len(nombre))
print(len("Hola mundo"))

##Los slices, traducidos al español 
#como “rebanadas”, nos permiten dividir
#los caracteres de un string de múltiples formas.

print(nombre[0:3])
#recorre del 0 al 7 pero toma de 2 en dos
print(nombre[0:7:2])

print(nombre[::])
##del primero hata el final de paso ede 3 en tres
print(nombre[1::3])
##del comienzo hasta el final pero retrocediendo de uno en uno
nombre2=nombre[::-1]
print(nombre2) 
