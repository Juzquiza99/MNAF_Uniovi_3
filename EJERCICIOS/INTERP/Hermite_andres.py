#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 13:53:45 2019

@author: andrespresavilla
"""

import numpy as np
import matplotlib.pyplot as plt

def hermite(x):
    n = len(x)
    L = np.zeros((n,n))
    phi1 = [] #añadiremos los de primer tipo
    phi2 = [] #añadiremos los de segundo tipo
    for i in range(n):
        suma=0
        y = np.delete(x,i)
        polinomio = np.poly(y) 
        denominador = np.polyval(polinomio,x[i]) 
        L[i] = polinomio/denominador #hasta aquí cálculo de los de Lagrange
        cuadrado = np.polymul(L[i],L[i]) #calculamos su cuadrado con polymul
        f=np.array([1,-x[i]])
        for k in range(n-1):
            suma = suma + 1/(x[i]-y[k])
        parent = 1-2*suma*np.array([1,-x[i]])
        phi1.append(np.polymul(parent,cuadrado)) #añadimos a la lista de los polin hermite 1
        phi2.append(np.polymul(f,cuadrado)) #añadimos a la lista los de segundo tipo
    PHI1=np.array(phi1) #los transformamos en arrays
    PHI2=np.array(phi2)
    return PHI1,PHI2

#Probamos un soporte de 5 elementos
x=np.random.rand(5)
x.sort() #les ordenamos
PHermite=hermite(x)[0]
print(PHermite)
X=np.linspace(0,1,201) 
Y=np.zeros((len(x),len(X))) 
for i in range(len(x)):
    Y[i,]=np.polyval(PHermite[i],X) #sustituimos los valores en el polinomio
fig=plt.figure(1,figsize=(4,3))
plt.plot(x,np.zeros(len(x)),'ro')
plt.plot(X,Y.transpose())
plt.title('Pol. fundamentales de Hermite')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(('Soporte',r'$H_4^{0}$',r'$H_4^{1}$',r'$H_4^{2}$',r'$H_4^{3}$',r'$H_4^{4}$'))
plt.grid()
plt.axis([0,1,-3,3])
plt.show()


