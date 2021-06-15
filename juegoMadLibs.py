import random
variable_random = random.randint(0,2)
adjetivo = input("Mencione un adjetivo: ")
mascota = input("Mencione una mascota: ")
verbo = input("Mencione un verbo: ")
if variable_random==0:
  print(f"El que este jugando este juego es {adjetivo},\n su mascota es {mascota}\n y le gusta {verbo}")
if variable_random==1:
  print(f"El que este jugando este juego es un {mascota}\n su mascota es {adjetivo}\n y tiene que {verbo} ")
if variable_random==2:
  print(f"El que este jugando es {adjetivo} y por eso el {mascota} lo va a {verbo}")
