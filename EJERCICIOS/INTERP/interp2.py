# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:52:45 2019

@author: UO264982

INTERPOLACIÓN POLINÓMICA

EJERCICIO 1
Dada la función f (x) = sin(x) en los puntos {0,1,2,3}, obtener y representar
la función, el soporte y el polinomio de interpolación utilizando instrucciones de Python.
"""

import numpy as N
import matplotlib.pyplot as plt
import scipy.interpolate as si

x=[0,1,2,3]
y=N.sin(x)
poly=si.lagrange(x,y) #Calculo del polinomio de interpolación usando polinomios de Lagrange
#Permite ahorraros el calculo po separado de la matriz de Vander.
#y de los coeficientes

X=N.linspace(x[0],x[-1],1000) # representación
Y=N.sin(X) # funcion
Z=poly(X)

#Vamos a calcularlo paso a paso:
V=N.vander(x) #Matriz de Vander
c=N.linalg.solve(V,y)
Z2=N.polyval(c,X) #Evaluamos los puntos en un polinomio de los coeficientes

fig=plt.figure(1)
plt.plot(x,y,'ro',label='Datos')
plt.plot(X,Y,'r',label='Función')
plt.plot(X,Z,'b',label='Lagrange Interpolate')
plt.plot(X,Z2,'y',label='Interpolación paso a paso')
plt.legend()
plt.title('Interpolación genérica', fontsize=20)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

'''EJERCICIO 2
Dada la función f (x) = x4−2x+1, obtener y representar la función y el
polinomio de interpolación cuando se utilizan 7 puntos de interpolación
esquiespaciados en el intervalo [−5,5].'''

x=N.linspace(-5,5,7)
y=x**4-2*x+1
poly=si.BarycentricInterpolator(x,y) #la función de interpolacion es la propia función
#porque al tener 7 puntos de intepolacion el polin de interp. es de grado 6 o menor,
#siendo la propia función. APROXIMACIÓN PERFECTA.

X=N.linspace(x[0],x[-1]) # representación
Y=X**4-2*X+1 # funcion
Z=poly(X)

fig=plt.figure(2)
plt.plot(x,y,'ro',X,Y)
plt.plot(X,Z)
plt.legend(('Datos','Interpolante Baricentro','función'))
plt.title('Interpolación genérica', fontsize=20)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#Ahora con la matriz de Van der Monde
V=N.vander(x)# matriz de Vandermonde
c=N.linalg.solve(V,y) # coeficientes del polinomio
Z=N.polyval(c,X) # interpolante
print(c) #Coeficientes de la función
#hagamos que aquellos que son prácticamente 0, sean 0
c[abs(c)<1e-10]=0
print(c)
#buscamos eliminar los 0s iniciales:
c=N.trim_zeros(c)
print(c)

fig=plt.figure(3)
plt.plot(x,y,'ro',X,Y)
plt.plot(X,Z)
plt.legend(('Datos','Interpolante','función'))
plt.title('Interpolación genérica', fontsize=20)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

'''
EJERCICIO 3
 Se realizan pruebas para determinar la relación entre esfuerzo (fuerza aplicada
al material por unidad de área) y deformación (de
exión por unidad de longitud)
en el mástil de un barco construido con una nueva aleación de aluminio.
 Los resultados se muestran en la siguiente tabla. σ (Kg/cm2) 126 365 506 527 562 703
                                                         δ (mm) 0,5 1,3 2 4,5 6 8,5
Calcular el polinomio de interpolación y comentar los resultados obtenidos
'''

x=N.array([126,365,506,527,562,703])
y=N.array([0.5,1.3,2,4.5,6,8.5])
poly=si.lagrange(x,y)
poly2=si.BarycentricInterpolator(x,y)
X=N.linspace(x[0],x[-1]) # representación
Z=poly(X)
Z2=poly2(X)

fig=plt.figure(4)
plt.plot(x,y,'ro',label='Datos')
plt.plot(X,Z, label='Interpolate Lagrange')
plt.plot(X,Z2, label='Interpolate Baricenter')
plt.legend()
plt.title('Interpolación genérica', fontsize=20)
plt.xlabel('x')
plt.ylabel('y')
plt.show()