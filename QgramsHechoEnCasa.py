def qGramsHechoEnCasa(palabra1,palabra2):
    porcentajeSimilitud = 0
    triadasPalabra1 =[]
    triadasPalabra2 = []
    for i in range(len(palabra1)):
        if i < len(palabra1)-2:
            triadasPalabra1.append(palabra1[i:i+3])
    for i in range(len(palabra2)):
        if i < len(palabra2)-2:
            triadasPalabra2.append(palabra2[i:i+3])
    cantidadDeTriadasComúnes = len(set(triadasPalabra1) & set(triadasPalabra2))
    listaConMásTriadas = max([len(triadasPalabra1),len(triadasPalabra2)])
    print(f"porcentaje de similitud = {round((cantidadDeTriadasComúnes/listaConMásTriadas)*100)} %")


qGramsHechoEnCasa("MiguelAngel","AngelMiguel")
