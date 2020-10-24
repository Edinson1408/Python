
def conversacion(mensaje):
    print('Hola')
    print('Como estas')
    print(mensaje)
    print('Adios')


opcion=int(input('Elige una opcion (1,2,3): '))
if opcion==1:
    conversacion('Elegistes la opcion 1')
elif opcion==2:
    conversacion('Elegistes la opcion 2')
elif opcion==3:
    conversacion('Elegistes la opcion 3')
else:
    print('Elije una opcion correcta')
