# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:45:39 2019

@author: javie
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so
from sympy.abc import x

#EJERCICIO 2
f = lambda x: x*np.exp(x)-4
t=np.linspace(a,b)
plt.figure()
plt.plot(t,f(t))
plt.grid()
plt.show()
a,b=0,2
maxiter, tolX, tolF = (1000,1E-6,1E-9)
#EJERCICIO 3
#BISECCIÓN
def bisec(fun,a,b,maxiter,tolx,tolf):
    fa=f(a) #Calculamos los valores de la función en dos puntos
    fb=f(b)
    if np.abs(fa)<tolf: #tenemos 1 cero
        return a
    if np.abs(fb)<tolf: #tenemos 1 cero
        return b
    if fa*fb>0:
        raise ValueError ('No se cumple el Teor. de Bolzano')
    else:
        for i in range(maxiter):
            c=(a+b)/2 #Calculamos el punto medio (xn)
            fc=f(c)
            if abs(fc)<tolf: #c está tan cerca de la raíz que lo damos por válido
                return c
             #si no, seguimos iterando
            elif (fa*fc)<0: #entonces la raíz está entre a y c
                    b=c #b pasa a ser c (acortamos el intervalo por la derecha)
                    fb=fc
                    if abs(c-a)<tolx: #el intervalo es tan pequeño que nos indica el cero
                        return c
            else: #la raíz estará entre c y b
                    a=c #a pasa a ser c
                    fa=fc
                    if abs(c-b)<tolx: #el intervalo es tan pequeño que nos indica el cero
                        return c
            

resul=bisec(f,a,b,maxiter, tolX, tolF)
print('Resultado método bisección:')
print (resul)


#REGULA FALSI
def regfal(fun,a,b,maxiter,tolx,tolf):
    fa=f(a) #Calculamos los valores de la función en dos puntos
    fb=f(b)
    if np.abs(fa)<tolf: #tenemos 1 cero
        return a
    if np.abs(fb)<tolf: #tenemos 1 cero
        return b
    if fa*fb>0:
        raise ValueError ('No se cumple el Teor. de Bolzano')
    else:
        for i in range(maxiter):
            c = a-fa*(b-a)/(fb-fa) #Calculamos xn
            fc=f(c)
            if abs(fc)<tolf: #c está tan cerca de la raíz que lo damos por válido
                return c
             #si no, seguimos iterando
            elif (fa*fc)<0: #entonces la raíz está entre a y c
                    b=c #b pasa a ser c (acortamos el intervalo por la derecha)
                    fb=fc
                    if abs(c-a)<tolx: #el intervalo es tan pequeño que nos indica el cero
                        return c
            else: #la raíz estará entre c y b
                    a=c #a pasa a ser c
                    fa=fc
                    if abs(c-b)<tolx: #el intervalo es tan pequeño que nos indica el cero
                        return c

resulfal=regfal(f,a,b,maxiter, tolX, tolF)
print('Resultado método regula falsi:')
print (resulfal)            
#EJERCICIO 4:
x2,s2= S.bisect(f,a,b,xtol=tolX,rtol=tolF, maxiter=maxiter,full_output=True )
print ('Bisect:')
print(x2,s2)

x3,s3=S.brentq(f,a,b,xtol=tolX,rtol=tolF, maxiter=maxiter,full_output=True)
print ('Brentq')
print (x3,s3)

x4,s4=S.brenth(f,a,b,xtol=tolX,rtol=tolF, maxiter=maxiter,full_output=True)
print ('Brenth')
print (x4,s4)

x5,s5=S.ridder(f,a,b,xtol=tolX,rtol=tolF, maxiter=maxiter,full_output=True)
print ('Ridder')
print (x5,s5)