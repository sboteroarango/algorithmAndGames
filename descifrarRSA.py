def descifradorRSA(numero):
    primerNumero = 0
    segundoNumero = 0
    lista1 = listaDePrimosHasta(numero)
    lista2 = lista1

    if not esPrimo(numero):
        for x in lista1:
            for i in range(len(lista2)):
                resultado = lista2[i]*x
                if resultado == numero:
                    primerNumero = x
                    segundoNumero = lista2[i] 
                    break
                
      
    else:
        print("el numero debe de ser compuesto")
    return primerNumero,segundoNumero

        

def listaDePrimosHasta(numero):
    lista = list(range(1,numero,1))
    listaReturn = []
    for i in lista:
        if esPrimo(i):
            listaReturn.append(i)
    return listaReturn


def esPrimo(numero):
    lista = list(range(1, numero+1,1))
    contador = 0
    for i in lista:
        if numero%i == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False

print(descifradorRSA(113*127))
