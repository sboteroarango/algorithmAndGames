#CREADOR DE NÚMEROS EN SECUENCIA

lista=input("deme una lista de números en secuencia")
listaideal=[]
listaideal.append(int(lista[0]))
listaideal.append(int(lista[1]))

for i in range(150):
    x=sum([listaideal[-1]+listaideal[-2]])
    listaideal.append(x)
print(listaideal)




