#buscar en todos los elementoa de manera secuencial
import random

def busqueda_lineal(lista,objeto):
    match=False

    for elemento in lista: #o(n) ya que se ejecuta un for 
        if elemento==objeto:
            match=True;
            break

    return  match


if __name__=='__main__':
    tamaño_de_lista=int(input('de que tamaño sera la lista ? :'))
    objetivo=int(input('que numero quieres encontrar? : '))

    lista=[random.randint(0,100) for i in range(tamaño_de_lista)]
    encontado=busqueda_lineal(lista,objetivo)
    print(lista)
    print(f'el elemento {objetivo} {"esta" if encontado  else "no esta" } en la lista')


