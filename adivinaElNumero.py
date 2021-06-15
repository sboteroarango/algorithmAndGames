import random
numero_a_adivinar = random.randint(0,100)
puntaje = 5000
puntaje_a_restar = 0
centinela = True
print("El numero es de 0-100")
print()
print()
while centinela:
  guess = int(input("Adivine el numero : "))
  if guess==numero_a_adivinar:
    print("ha adivinado el número")
    centinela=False
  if guess<numero_a_adivinar:
    print("el número es mayor")
    print()
    puntaje_a_restar += 50
  if guess>numero_a_adivinar:
    print("el número es menor")
    print()
    puntaje_a_restar += 50

print(f"\n\nel número era {numero_a_adivinar}\nsu puntaje es de {puntaje-puntaje_a_restar}\nmuchas gracias por jugar")
