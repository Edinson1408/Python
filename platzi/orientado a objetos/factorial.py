#factoriales son 10! = 10*9*8*7*6*5*4*3*2*1

def factoriales(numero):
    if numero==0:
        return 1
    else:
         return numero*factoriales(numero-1)
        

#veamos
# 10 es igual a 0 
# no
# 10 * factorial (9) 
#     9= 0 no
#     9*factoriales(8)
#         8=0

print(factoriales(10))