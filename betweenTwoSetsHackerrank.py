def getTotalX(a, b):
    factoresDeB = []
    factoresComunesDeB = []
    totalDeNumerosCasiEspeciales = []
    totalDeNumerosEspeciales = []
    for i in range(1,b[0]+1,1):
        for numero in b:
            if numero%i==0:
                factoresDeB.append(i)
    for i in range(1,b[0]+1,1):
        if factoresDeB.count(i)>=len(b):
            factoresComunesDeB.append(i)
    for factorComun in factoresComunesDeB:
        for entero in a:
            if factorComun%entero ==0:
                totalDeNumerosCasiEspeciales.append(factorComun)
    for factorComun in factoresComunesDeB:
        if totalDeNumerosCasiEspeciales.count(factorComun)>= len(a):
            totalDeNumerosEspeciales.append(factorComun)
    print(totalDeNumerosEspeciales)      
    return len(totalDeNumerosEspeciales)
    
