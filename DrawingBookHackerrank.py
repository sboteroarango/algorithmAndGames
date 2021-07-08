def pageCount(n, p):
    lista = [[1]]
    formadorDeLista1 = 2
    formadorDeLista2 = 4
    while formadorDeLista1<= n:
        lista.append(list(range(formadorDeLista1,formadorDeLista2)))
        formadorDeLista1+=2
        formadorDeLista2+=2
    if n+1 in lista[-1]:
        lista[-1].pop(1)
        
    contadorDeSlicesHaciaDerecha = -1
    contadorDeSlicesHaciaIzquierda = -1
    for i in lista:
        contadorDeSlicesHaciaDerecha +=1
        if p in i:
            break
    for i in range(len(lista)-1,-1,-1):
        contadorDeSlicesHaciaIzquierda+=1
        if p in lista[i]:
            break
    return min([contadorDeSlicesHaciaDerecha,contadorDeSlicesHaciaIzquierda])
