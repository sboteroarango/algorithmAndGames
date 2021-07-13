from itertools import permutations
#ingresar un string y el tamaño de las permutaciones, separados por espacio (HACK 2)
string, n = input().split()
string = sorted(string)
n = int(n)
lista = list(permutations(string,n))
for i in lista:
    print(''.join(i))
