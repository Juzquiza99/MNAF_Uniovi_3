# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:54:41 2019

@author: UO264982
"""

#EJ. POLINOMIO LAGRANGE I
import numpy as np
import matplotlib.pyplot as plt 

'''F lagrange para todos los puntos menos 1 de los dados'''

def lagrange(x):
    n = len(x)
    L = np.zeros((n,n))
    for i in range(n):
        y = np.delete(x,i)
        polinomio = np.poly(y)
        denominador = np.polyval(polinomio,x[i])
        L[i] = polinomio/denominador
    return L 

#Defnición del soporte y cálculos
x=np.random.rand(5)
x.sort() #Ordena los elementos de la lista de menor a mayor

PLag=lagrange(x)



#Representación
X=np.linspace(0,1,201)
Y=np.zeros((len(x),len(X)))
for i in range(len(x)):
    Y[i,]=np.polyval(PLag[i],X)

#Sumatorio de las funciones de los polinomios de Lagrange
T=np.zeros(len(X))
for i in range(len(X)):
    T[i]=np.sum(Y[:,i])  

  
fig=plt.figure(1,figsize=(4,3))
plt.plot(x,np.zeros(len(x)),'ro')
plt.plot(X,Y.transpose())
plt.plot(X,T,label='Sumatorio')
plt.title('Pol. fundamentales de Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(('Soporte',r'$L_4^{0}$',r'$L_4^{1}$',r'$L_4^{2}$',r'$L_4^{3}$',r'$L_4^{4}$'))
plt.grid()
plt.axis([0,1,-3,3])
plt.show()


#EJERCICIO 5
p=[1,0,0,-2,1]
x=np.linspace(-5,5,7)
y=np.polyval(p,x)


PLag=lagrange(x)
print(PLag)
P=np.dot(y,PLag) #Coeficientes
print(P)
X=np.linspace(-5,5,201)
Z=np.polyval(P,X)
Y=np.polyval(p,X)

plt.figure()
plt.plot(x,y,'ro')
plt.plot(X,Z,label='Interpolante')
plt.plot(X,Y,label='Función')
plt.legend()
plt.grid()
plt.show()
