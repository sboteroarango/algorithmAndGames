import random
from datetime import datetime, timedelta

texto = ''
caracteresDelTexto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(5):
    texto = texto + caracteresDelTexto[random.randint(0,len(caracteresDelTexto)-1)]

print()
print()
print(texto)
print()
print()
print()
print('Comienze a escribir \n')
horaComienzo = datetime.now()
print()
respuesta = input()
horaFinal = datetime.now()

errores = 0
for indice in range(len(respuesta)):
    try:
        if texto[indice]!= respuesta[indice]:
            errores+=1
    except:
         errores+=1
if len(respuesta)<len(texto):
    errores += len(texto)-len(respuesta)

porcentajeDePrecision = 100 - ((errores/len(texto))*100)


print()
print(f'PRECISION = {porcentajeDePrecision}%\n')
print(f'VELOCIDAD = {len(respuesta)/int((horaFinal-horaComienzo).seconds)} letras/segundos')


