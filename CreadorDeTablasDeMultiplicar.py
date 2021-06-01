#CREADOR DE TABLAS DE MULTIPLICAR

def creadordetablasdemultiplicar(a,b):
    tablas=[]
    rango=range(1,b+1,1)
    for x in rango:
        tablas.append(a*x)
    return (tablas)
print(creadordetablasdemultiplicar(3.14,10))
