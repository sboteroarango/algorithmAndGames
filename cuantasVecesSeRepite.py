from collections import Counter
n = int(input())
lista = []
for i in range(n):
    lista.append(input())
counter = Counter(lista)

print(f'hay {len(counter)} valores distintos')
#*retorna lo que esta adentro del objeto que se imprime
print('sus veces de aparicion son respectivamente: ')
print(*counter.values())
