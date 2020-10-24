nombre=input('Escrbi el nombre : ')
respuesta='';

if nombre=="Espatifilo":
    respuesta='Si, ¡El Espatifilo es la mejor planta de todos los tiempos!'
elif nombre=='espatifilo':
        respuesta='No, ¡quiero un gran Espatifilo!'
else:
    respuesta="¡Espatifilo! ¡No "+nombre+"!";
    

print(respuesta);



ingreso=float(input("Ingrese el ingreso anual:"))

#
# Coloca tu código aquí.
#
if ingreso<85528:
    impuesto=(ingreso*0.18)-556.2
else:
    impuesto=14839.2+((ingreso-85528)*0.32)

if impuesto<0:
    impuesto=0.0

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")

#---

año = int(input("Introduzca un año:"))

#
# Coloca tu código aquí.
#



if (año%4)!=0:
    respuesta='Año comun'
elif  (año%100)!=0:
    respuesta='Año bisiesto'
elif (año%400)!=0:
    respuesta='Año Año comun'
else :
    respuesta='Año bisiesto'

if año<1582:
    respuesta='No dentro del período del calendario gregoriano'
    
    
print(respuesta)
