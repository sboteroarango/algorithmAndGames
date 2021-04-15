import matplotlib.pyplot as plt

ci=int(input("cual es su capital inicial: "))
ganancia=int(input("ingrese su porcentaje de ganancia anual: "))
tiempo=int(input("por cuanto tiempo es la inversión: "))
tiempo+=1
ganancia=ganancia/100
cf=[]
sarmiento=[]
for i in range(tiempo):
    tiempox=i
    final=ci*(1+ganancia)**tiempox
    final=round(final)
    cf.append(final)
    sarmiento.append(8439705420781881344)
x=list(range(0,tiempo,1))
plt.plot(x,cf,label="Mi capital")
plt.plot(x,sarmiento,label="Capital de Sarmiento")
plt.title("Yo vs Sarmiento")
plt.show()
plt.plot(x,cf,label=f'El capital final es:$  {cf[-1]:,.2f}')
plt.title("Mi capital solo")
plt.legend()
plt.show()
