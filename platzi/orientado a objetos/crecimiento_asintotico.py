#no importa variociones pequeñas
#el enfoque se cnetra en lo que pase conforme el tamaño del problema se acerca al infinito
#mejor de los casos promedio peor de los casos
#big0
#nada mas importante el termino de mayor tamaño (termino dominates)

#ley de suma
def f(n):
    for i in range(n):
        print(n)
    
    for i in range(n):
        print(i)
    
#0(n)+ o(n) = 0 (n+n) =0(2n)  = o(n) al final la funcion crece eno de n - > de forma lineal

def f(n):
    for i in range(n):
        print(i)
    
    for i in range(n*n):
        print(i)

#0(n)+o(n*n)=0(n+n2)= 0(n2)

def f(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

#o(n) * o(n) =0(n*n)= 0(n2)
#crecen de forma cuadratica


def fibonacci(n):
    if n==0 or n==1:
        return 1
    
    return fibonacci(n-1)+fibonacci(n-1)

    #o(2**n) cuanod es recursivo es 2 al exponente n 
    #por que ejecutaremos dos llamadas recursivas n veces
    #crecimiento expontencial
    

        