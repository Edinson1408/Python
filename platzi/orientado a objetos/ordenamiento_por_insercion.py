# El ordenamiento por inserción es uno de los algoritmos más comunes que estudian
# los Científicos del Cómputo. Es intuitivo y fácil de implementar, pero es muy
# ineficiente para listas de gran tamaño.

# Una de las características del ordenamiento por inserción es que ordena en “su
# lugar.” Es decir, no requiere memoria adicional para realizar el ordenamiento
# ya que simplemente modifican los valores en memoria.

def ordenamiento_por_insercion(lista):
    # lista_desordenada=lista
    # lista_ordenada[lista[0]]
    n=len(lista)
    for i in range(1,n): #recorremos de la segunda posicion
        posicion_actual=i #tenemos la posicion acual o el indice
        valor_actual=lista[i]  # ontemoes el valor actual

        while posicion_actual>0 and lista[posicion_actual-1]>valor_actual: #decimos que el indice sea mayor que 0 y que un indice anterior(posicion=1 -1 da la posicion 0)
            #evalua la posicion 0 entonces es mejor 
            lista[posicion_actual]=lista[posicion_actual-1]#si es menor la cambia d eposicion por que la anteiror es mayor a la acual esto dice que mi posicion 1 no es la accutal si no la antriror por que es mayor:

            posicion_actual-=1 # disminuimos la posicion anctual para que vaya recuriendo hacia atras

        lista[posicion_actual]=valor_actual
    
    return lista

Lista=[7, 3, 2, 9, 8]
print(Lista)
lista_2=ordenamiento_por_insercion(Lista)
print(lista_2)