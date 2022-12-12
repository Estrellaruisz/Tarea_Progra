import random
a=[]
for i in range(0,10):
    num=random.randint(1,100)
    a.append(num)
print("Los elementos del arreglo son:",a)
print("") #dejar una linea en blanco
print("En orden inverso")
for i in reversed(a):
    print("El orden inverso:",i)