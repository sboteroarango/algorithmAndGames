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
