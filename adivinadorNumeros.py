import random

def esta_en_numeros_prohibidos(x):
  if x in numeros_prohibidos:
    return True
  else:
    return False

print("piense un numero del 1 al 10")
centinela = True
numeros_prohibidos = []
intentos = 0
while centinela:
  if intentos==10:
    print("tu numero no existe")
    break
  numero = random.randint(1,10)
  if esta_en_numeros_prohibidos(numero):
    continue
  respuesta = input(f"su numero es {numero}? si/no ")
  if respuesta=="si":
    centinela= False
  if respuesta=="no":
    numeros_prohibidos.append(numero)
    intentos += 1
if intentos==10:
  print()
else:
  print(f"\n\nLO ADIVINE EN {intentos+1} INTENTOS, GRACIAS POR JUGAR")
