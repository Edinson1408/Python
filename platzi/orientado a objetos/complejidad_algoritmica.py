#permite comprar la eficiencia entre dos algoritmios
#para poder saber el tiempo que se tomara el algoritmo(resolver algoritmo)

#por que comparamos la eficioente un algoritmo 
#complejidada temporal vs complejidad espacial
#podemos definirla como T(n)
#/////////////////////////////////////////////
#aproximaciones 
#cromometrar el timpo en que corre un algoritmo
#contat los pasoa con una medidad abtracta de operacion
#contar los paso conforme nos aproxima al infinito
import time #modulo para medir el tiempo

def factorial(n):
    respuesta=1
    while n>1:
        respuesta*=n
        n -=1
    return respuesta

def factorial_r(n):
    if n==1:
        return 1
    return n*factorial(n-1)

if __name__=='__main__':
    n=200000

    comienzo=time.time()
    factorial(n)
    #print(factorial(n))
    final=time.time()
    print(final-comienzo)

    comienzo=time.time()
    factorial_r(n)
    #print(factorial_r(n))
    final=time.time()
    print(final-comienzo)
