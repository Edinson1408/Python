#agregar un booleeano
#asegurarnos que le usuario no comenta un error
#ejemplo tu tiene una suma de numero enteros
#el pendejo del usuario te envia un texto
#mandas un mensaje no se permite string solo numero

def primera_letra(lista_de_palabras):
    primeras_letras=[]
    for palabra in lista_de_palabras:
        assert type(palabra)== str ,f'{palabra} no es Str'
        assert len(palabra)>0 ,'No se permite str vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras

lista_de_palabras=['hola','uno']
print(primera_letra(lista_de_palabras))
    
print('123' + '456')

print(5 / 'Platzi')

print (‘123’ + ‘456’)
