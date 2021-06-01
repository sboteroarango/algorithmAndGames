#CREADOR DE 150 NÚMEROS EN SECUENCIA

lista=input("deme una lista de números en secuencia")
listaideal=[]
listaideal.append(int(lista[0]))
listaideal.append(int(lista[1]))

for i in range(150):
    x=sum([listaideal[-1]+listaideal[-2]])
    listaideal.append(x)
print(listaideal)
"""
#JUEGO DE DADOS

import random

nombre1=str(input("ingrese su nombre"))
nombre2=str(input("ingrese su nombre"))
print("gana el que acierte primero el objetivo de la suma de los 2 dados primero")
objetivo=random.randint(1,12)
print("el objetivo de la suma es: ",objetivo)
points1=0
points2=0
invitacion=input("Quiere jugar(si/no)")
while (points1<1 or points2<1) and invitacion=="si":
    dado1_1=random.randint(1,6)
    dado1_2=random.randint(1,6)
    dado2_1=random.randint(1,6)
    dado2_2=random.randint(1,6)

    print("los resultado de ",nombre1," son iguales a ",dado1_1,"y ",dado1_2)
    print("los resultado de ",nombre2," son iguales a ",dado2_1,"y ",dado2_2)

    suma1=dado1_1+dado1_2
    suma2=dado2_1+dado2_2

    if suma1==objetivo:
        points1+=1
    else:
        print("fallaste,",nombre1, "tu suma es ",suma1)
        pass
    if suma2==objetivo:
        points2+=1
    else:
        print("fallaste,",nombre2, "tu suma es ", suma2)
        pass
    pregunta= input("Quieres continuar (si/no)")
    if pregunta=="si":
        continue
    if pregunta=="no":
        break
    
if points1==1:
    print("el ganador es ",nombre1)
elif points2==1:
    print("el ganador es", nombre2)
else:
    print("juego terminado")

#ENCONTRADOR DE AÑOS BISIESTOS
"""
def esbisisiesto(año):
    if (año%4)==0:
        if (año%100)==0:
            if (año%400)==0:
                return año," es bisiesto"
            return año," no es bisiesto"
        
        return año," es bisiesto"
    return año, " no es bisiesto"
aso=print(esbisisiesto(4000))


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

