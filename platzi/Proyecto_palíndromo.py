def es_palindromo(palabra):
    
    palabra=palabra.upper()
    palabra=palabra.replace(' ','')
    
    palabra2=palabra[::-1]
    
##    print(palabra2)
    if palabra==palabra2:
       print("Es palindromo")
    else:
        print("No Es palindromo")

palabra= str(input("Ingrese una palabra: "))

##print(palabra[::-1])

es_palindromo(palabra)
