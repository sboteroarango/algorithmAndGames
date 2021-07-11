def beautifulDays(i, j, k):
    def reversar(numero):
        numero = str(numero)
        listaDelNumero = []
        for digito in numero:
            listaDelNumero.insert(0,digito)
        numero = ''.join(listaDelNumero)
        numero = int(numero)
        return numero
    
    listaDias = list(range(i,j+1))
    conteo = 0
    for dia in listaDias:
        if abs(dia-reversar(dia))%k == 0:
            conteo += 1
    return conteo
