# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:22:06 2019

@author: UO264982
"""

import numpy as np
import numpy.linalg as la
import scipy.optimize as so

#APLICACIÓN-PÁG 13-14
def func(X):
    x,y,z = X
    f1=(x/10)**2+((y+10)/10)**2+(z/4)**2-1
    f2=(x/40)**2+((y-20)/25)**2+(z/5)**2-1
    f3=((y+5)/2)**2+(z/2)**2-1
    f=np.array([f1,f2,f3])
    return f

v=np.array([0.,0.,0.]) #Definimos el punto en el que comienza a iterar
print (func(v))

print('Solución:')
sol=so.root(func,v)
print(sol)


'''
AUTOVALORES Y AUTOVECTORES
MET 1: potencia, nos permite calcular el radio espectral
Introducimos una matriz A  y queremos que nos devuelva sus autovalores
'''
def autovmax(A):
    fA,cA=A.shape
    wr=np.random.rand(fA)
    nor=la.norm(wr)
    w0=wr/nor #vector de norma 1
    u=np.array(A.shape)
    w=w0
    for i in range(99):#Número de iteraciones
        u=np.dot(A,w)
        w=u/la.norm(u)
        land1=la.multi_dot([w.transpose(),A,w])
    return land1    


print('Por el método de la potencia:')
print(autovmax(A))
print('Por linalg:')
print(la.eigvals(A))


def autovmin(A):
    fA,cA=A.shape
    wr=np.random.rand(fA)
    nor=la.norm(wr)
    w0=wr/nor #vector de norma 1
    u=np.array(A.shape)
    w=w0
    for i in range(99):#Número de iteraciones
        u=np.dot(la.inv(A),w)
        w=u/la.norm(u)
        land1=la.multi_dot([w.transpose(),la.inv(A),w])
    return 1./land1        

A=np.array([[1,9,3,2],[2,3,1,1],[3,7,1,8],[2,9,5,4]])
print('Por el método de la potencia inversa:')
print(autovmin(A))
print('Por linalg:')
print(la.eigvals(A))
