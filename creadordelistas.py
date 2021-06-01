#CREADOR DE NÚMEROS EN SECUENCIA

lista=input("deme una lista de números en secuencia")
listaideal=[]
listaideal.append(int(lista[0]))
listaideal.append(int(lista[1]))

for i in range(150):
    x=sum([listaideal[-1]+listaideal[-2]])
    listaideal.append(x)
print(listaideal)





#VALIDADOR DE CONTRASEÑAS

contraseña=input("ingrese su contraseña:")
validacion=True
while validacion==True:
    if len(contraseña)<8:
        print("contraseña incorrecta")
        validacion=False
    elif contraseña.isalnum==True:
        print("contraseña incorrecta")
        validacion=False
    elif contraseña.islower==True:
        print("contraseña incorrecta")
        validacion=False
    elif  contraseña.isupper()==True:
        print("contraseña incorrecta")
        validacion=False
    elif contraseña.isnumeric()==True:
        print("contraseña incorrecta")
        validacion=False
    elif " " in contraseña:
        print("contraseña incorrecta")
        validacion=False
    else:
        print("contraseña correcta")
        validacion=False


#CREADOR DE TABLAS DE MULTIPLICAR

def creadordetablasdemultiplicar(a,b):
    tablas=[]
    rango=range(1,b+1,1)
    for x in rango:
        tablas.append(a*x)
    return (tablas)
print(creadordetablasdemultiplicar(3.14,10))

