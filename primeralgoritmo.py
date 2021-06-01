#este algoritmo revisa que los parentesis cuadren y simplifica la preposición lógica
preposición=input("Coloca una preposición sin espacios entre caracteres: ")
abiertos=0
cerrados=0
a="abcdefghijklmnñopqrstuvwxyz"
for i in preposición:
    if i=="(":
        abiertos+=1
    elif i==")":
        cerrados+=1      
    elif i in a:
        índice=a.index(i)
        preposición=preposición.replace(("(-("+a[índice]+"))"),("-("+a[índice]+")"))
        preposición=preposición.replace(("("+a[índice]+")"),(a[índice]))
    else:
        continue        
respuesta=abiertos-cerrados
if respuesta==0:
    print("si cumplen los parentesis")
else:
    print("no cumplen los parentesis")
print("la preposición simplificada es:"+preposición)
