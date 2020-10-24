bloques = int(input("Ingrese el número de bloques:"))

#
# Escribe tu código aquí.
#
altura=0
Contador=1
while bloques>0:
    bloques=bloques-Contador
    if bloques<0:
        break
    Contador=Contador+1
    altura=altura+1

print("La altura de la pirámide:", altura)
