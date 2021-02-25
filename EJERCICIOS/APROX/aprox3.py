# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:25:30 2019

@author: UO264982
"""

import numpy as np
import scipy.integrate as si
import numpy.linalg as la
import matplotlib.pyplot as pl

#EJEMPLO 5

a=np.array([[155,173,143],[83,92,75],[55,76,57],[59,29,38]])
t=[9120,4830,3570,2610]
sol=la.lstsq(a,t,rcond=None)
print(sol)

#POLINÓMICA

def aproxmc1c(base,a,b,fun):
    n=len(base)
    G=np.zeros((n,n))
    f=np.zeros(n)
    
    for i in range(n):
        elef=si.quad(lambda x: base[i](x)*fun(x),a,b)
        f[i]=elef[0]
        for j in range(i,n):
            eleg=si.quad(lambda x:base[i](x)*base[j](x),a,b)
            G[i,j]=eleg[0]
            G[j,i]=G[i,j]
    return G,f

base1=[lambda x: np.ones_like(x), lambda x: x, lambda x: x**2-1./3, lambda x: x**3-(3./5)*x]
fun1=lambda x: np.ones_like(x)
print(aproxmc1c(base1,-1,1,fun1))

#☺Se cumple que es ortogonal si todos las posiciones de la matriz son nulas salvo las de la diagonal
