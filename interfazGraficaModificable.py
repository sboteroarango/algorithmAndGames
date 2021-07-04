print('Ingrese el largo y el ancho de la interfaz que desea como 2 numeros impares separados por espacio, donde el segundo es el primero por 3 ej:(7 21) :')
datos = input().split()
N,M = int(datos[0]), int(datos[1])
simbolo = ''

for i in range(int((N-1)/2)):
    simbolo = '.|.' * (2*(i)+1)
    print('-'*(int((M-len(simbolo))/2))+simbolo+'-'*(int((M-len(simbolo))/2)))

print('-'*(int((M-7)/2))+'WELCOME'+'-'*(int((M-7)/2)))

for i in range(int((N-1)/2)):
    print('-'*(int((M-len(simbolo))/2))+simbolo+'-'*(int((M-len(simbolo))/2)))
    simbolo = simbolo.replace('.|.'*2,'',1)
    
