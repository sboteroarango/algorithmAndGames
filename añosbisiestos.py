#ENCONTRADOR DE AÑOS BISIESTOS

def esbisisiesto(año):
    if (año%4)==0:
        if (año%100)==0:
            if (año%400)==0:
                return año," es bisiesto"
            return año," no es bisiesto"
        
        return año," es bisiesto"
    return año, " no es bisiesto"
aso=print(esbisisiesto(4000))
