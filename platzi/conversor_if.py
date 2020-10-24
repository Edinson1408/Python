menu ="""
Bienvenido al converzor de monera  ;
1 : Pesos colombianos
2 : Pesos argentinos
3 : Pesos mexicanos
Elije una opcion:  """;

n=0;
opcion=int(input(menu));

if opcion==1:
    Nombre="Pesos Colombianos"
    valor_dolar=3875;
    
elif opcion==2:
    Nombre=float(input("Cuantos pesos colombianos tienes : "))
    Nombre="Pesos Argentinos";
    valor_dolar=65;
    
elif opcion==3:
    Nombre=float(input("Cuantos pesos colombianos tienes : "))
    valor_dolar=24;
    
else :
    n=1;
    print("Ingresa una opcion correta por favor");
    
   
if n==1 :
    pass
else :
    pesos=float(input("Cuantos" + Nombre + "  tienes : "))
    dolares= pesos/valor_dolar
    dolares=round(dolares,2)
    print("Tines $ " + str(dolares) + "Dolares");

    


