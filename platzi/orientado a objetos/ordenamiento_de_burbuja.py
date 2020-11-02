# el ordenamiento de burbuja es un algorimo que recorre repitidamente una lista que necesita ordenarse.
# compara elementos adyacentes y los intercanbian si estan en el orden incorrecto .
# este procedimiento se repite hasta que no se requieren mas interambios , lo que indica que la lista se encuentra ordenada

#evaluda cada uno de los elementos , y lo empezamos aintercambiar para poner orden de menor a mayor

import random

def ordenamiento_de_burbuja(lista):
    n=len(lista)

    for i in range(n):
        for j in range(0,n-i-1): #o(n)*o(n) = o(n**2)  crecimiento polinominial

            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista

if __name__=='__main__':
    tamano_lista=int(input('De que tamaño es la lista: '))

    lista=[random.randint(0,100) for i in range(tamano_lista)]
    print(lista)

    lista_ordenda=ordenamiento_de_burbuja(lista)
    print(lista_ordenda)
    