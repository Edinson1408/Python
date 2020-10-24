##def factorial(numero):
##    
##        
##    return numero*factorial(numero-1)
##    
##    
##
##def factosus(numero):
##    return int(numero-1)
##
##factorial_var=int(input("iintroduce el numero para caulcular su factorial "))
##
##
##numero_factorial=factorial(factorial_var)
##    
##    
##print(numero_factorial)
##    

def funcion1(numero):
    if numero==1 :
        return 1
    print(numero)
    return numero*funcion1(numero-1)
    
    


print(funcion1(4))





