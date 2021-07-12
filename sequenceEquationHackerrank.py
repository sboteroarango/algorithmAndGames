def permutationEquation(p):
    listaDePs = []
    respuesta = []
    for x in range(1,len(p)+1):
        listaDePs.append(f'p({x})')
    for x in range(1,len(p)+1):
        indice = p.index(x)
        pes = listaDePs[indice]
        valorAdentroDePes = int(pes[pes.find('(')+1:pes.find(')')])
        indiceParaAgregar = p.index(valorAdentroDePes)
        valorFinal = listaDePs[indiceParaAgregar]
        respuesta.append(int(valorFinal[valorFinal.find('(')+1:valorFinal.find(')')]))
    return respuesta
