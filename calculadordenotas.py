cantidadexamenes=int(input("Cuantos exámenes ha tenido: "))
respuesta=0
porcentajetotal=0
for i in range(cantidadexamenes):
    porcentaje=int(input(f"Cuantos por ciento vale el examen {i} :"))
    porcentajetotal=porcentaje+porcentajetotal
    nota=float(input(f"Cuantos sacó en el examen {i} :"))
    respuesta=respuesta+(nota*(porcentaje/100))
print(f"su calificación actual es de {respuesta}")
print(f"le falta {100-porcentajetotal} % del curso")
notanecesaria=(3-respuesta)/((100-porcentajetotal)/100)
if(notanecesaria>0):
    print(f"su nota debe ser {notanecesaria} para obtener 3")
else:
    print("Ya ha ganado el curso")
