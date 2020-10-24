def es_primo(numero):
    contador=0
    for x in range(1,numero+1):
        if  numero%x==0:
            contador=contador+1
            
        
    if contador==2 or numero==1:
        return True
    else:
        return False
        
    
def run():
    numero=int(input("Escruba un numero : "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")

if __name__== '__main__':
    run()

        
