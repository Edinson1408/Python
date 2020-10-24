my_dic ={
    'David' : 35,
    'Erika' : 32,
    'Jaime' : 50
    }

print(my_dic['David'])

my_dic.get('Juan',30)

print(my_dic.get('Juan',30))

my_dic['Jaime']=20;

print(my_dic)

my_dic['Pedro']=70

print(my_dic)

del my_dic['Jaime']

print(my_dic)

for llave in my_dic.keys():
    print(llave)

for valor in  my_dic.values():
    print(valor)

for llave,valor in my_dic.items():
    print(llave,valor)

#saber si una llave esta incluida denteo de un diccionario

print('David' in my_dic)
print('Edinson' in my_dic)
