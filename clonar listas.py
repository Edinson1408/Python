a=[1,2,3,]
id(a)
b=a
c=list(a)

d=a[::]
print(d)
# id es donde guarda en memoria
print(id(a))
print(id(d))


my_list =list(range(100))
print(my_list)
double =[i * 2 for i in my_list]
print(double)
    

pares=[i for i in my_list if i %2==0]

print(pares)
