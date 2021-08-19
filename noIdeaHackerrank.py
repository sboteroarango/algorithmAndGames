# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
array = list(map(int, input().split()))
conjuntoA = set(map(int, input().split()))
conjuntoB = set(map(int, input().split()))

contador = 0

for x in array:
    if x in conjuntoA:
        contador+=1
    if x in conjuntoB:
        contador-=1
        
print(contador)
