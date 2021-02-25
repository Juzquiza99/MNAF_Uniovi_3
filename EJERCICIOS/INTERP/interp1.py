# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:24:01 2019

@author: UO264982
"""

import numpy as np
import matplotlib.pyplot as plt

#Definimos la base sobre la que vamos a trabajar:
base=lambda x:[np.sin(x),np.cos(x),np.ones(np.size(x)),np.log1p(x)]
x=[1,2,3,4] #puntos
y=np.power(x,2) #f(puntos)

#Evaluación
yeval=base(x) #nos devuelve un array de arrays con los puntos x evaluados en la base
print(yeval)

A=np.vstack(yeval) # Conversion a matriz
A=np.transpose(A)

c=np.linalg.solve(A,y) # coeficientes de la solución del proble Ax=b

#Representación
X = np.arange(0.0, 5.0, 0.05)
Y = np.vstack(base(X)) 
Y=np.dot(c,Y)
fig=plt.figure(1)
plt.plot(x,y,'ro',X,Y)
plt.plot(X,X**2)
plt.legend(('Datos','Interpolante','función'))
plt.title('Interpolación genérica', fontsize=20)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
