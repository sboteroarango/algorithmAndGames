from collections import Counter
def migratoryBirds(arr):
    diccionario = dict(Counter(arr))
    frecuencias = list(diccionario.values())
    mayorFrecuencia = max(frecuencias)
    idsConMayorFrecuencia = []
    for key,value in diccionario.items():
        if value==mayorFrecuencia:
            idsConMayorFrecuencia.append(key)
    return min(idsConMayorFrecuencia)
