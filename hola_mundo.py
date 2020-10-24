print ("hola");
print ("bien venido a funcamentos d eprogramacion en python")
print("esto esta hecho en mi pc")

##--//*para poner un dato al final*/

print("hola soy ", end="final")
print()
##para poner un cracter por cadad concatenacion
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

print("Fundamentos","Programación","en",end="...",sep="***")
print("Python")

#python permite numerop octales y hexadecimales
print(0o123)
print(0x123)



print(2.5)

print(.4)

# el valor E o e es para poner un exponente 3 x 10elvado 8
print(3E8)

##6.62607 x 10-34. LAMENTABLEMENTE NO SE PODRA XD 
print(6.62607E-34)

print(0.0000000000000000000001)
print(1e-22)
##la coma es interpretada como espacio

print(2,5)

## \ para poner unas comillas dentro de otra comillas es un comodin
print("Me gusta \"Monty Python\"")

## Esto tambien ayudara , utilizar comillas simples al principio y al final 

print('Me gusta "Monty Python"')

print('I\'m Monty Python. ')

##bollenanos  true y false o 1 y 0
print(0==0)

##Laboratorio
print ('"Estoy"')
print ("\"\"Aprendiendo\"\"")
print ("\"\"\"Python\"\"\"")

##
print(1011)


print(2+2) #suma
print(2-2) #Resta
print(2*2.3) #Multiplicacion
print(2/2) #diviion

print(2//2)  #divicion entera
print(2%2)  #Residuo
print(2**2.3)  #exponente

print(2 + 3 * 5)

##print(2 ** 2 ** 3)  lo que ghra es correrlo desde la derecha 2 ** 3 → 8; 2 ** 8 → 256
##primero hara 2**3 = 8 y luego remplazar 2**8 dando resultado de 256


print(2 ** 2 ** 3)


##en este caso * % teiene la misma prioridad pero toma de izquier a derecha
print(2 * 3 % 5)

#si tiene variable edinson y EDINSON pyton interpreta dos cosas distintas
## crre que son variables diferentes 


kilometros = 12.25
millas = 7.38

millas_a_kilometros =millas*1.61
kilometros_a_millas = kilometros/1.61

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")



##mira como puedes divir un numero
a = 6
b = 3
a /= 2 * b
print(a)

##como utilizar una funcion

print("Dime algo...")
algo = input()
print("Mmm...", algo, "...¿en serio?")

## imput() sirve par imgresar algp


print('sumare')
print('primer numero')
num1=int(input())
print('segundo numero')
num2=int(input())
suma=num1+num2
print('La suama de los numeros es: ',suma)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


