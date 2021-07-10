
cube = lambda n: n**3

def fibonacci(x):
    lista = [0,1]
    if x == 0:
        lista = []
    elif x == 1:
        lista = [lista[0]]
    elif x == 2:
        lista = lista
    else:
        for i in range(2,x,1):
            lista.append(lista[i-1]+lista[i-2])
    return lista
