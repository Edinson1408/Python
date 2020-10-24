numero=int(input("Escriba un numero positivo entero : "))
pasos=0;
if (numero>0) :
    c0=numero;
    while c0!=1:
        pasos=pasos+1;
        if c0%2==0:
            c0=c0 / 2
            print(int(c0))
        else:
            c0=3*c0 + 1 
            print(int(c0))
    
    
else :
    print("Porfavor escriba un numero positivo")

print("pasos ", pasos)
