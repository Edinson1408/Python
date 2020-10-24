# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.
userWord='Gregory'
userWord = userWord.upper()
for letra in userWord:
    # Completa el cuerpo del ciclo for.
    if letra=='A' or letra=='E' or letra=='I' or letra=='O' or letra=='U':
        continue
    else:
        print(letra)
        
    


palabraSinVocal = ""

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord
userWord='IOUEA'
userWord=userWord.upper()

for letra in userWord:
	# Completa el cuerpo del ciclo.
	if letra=='A' or letra=='E' or letra=='I' or letra=='O' or letra=='U':
	    continue
	else:
	    palabraSinVocal=palabraSinVocal+letra

print(palabraSinVocal)
# Imprimir la palabra asignada a palabraSinVocal.
