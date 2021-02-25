# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:20:57 2019

@author: UO264982
"""

import sympy as S
import numpy as N
import matplotlib.pyplot as plt
x=S.symbols('x',real=True)

#g1
gs=(x**2*S.exp(x)+4)/S.exp(x)/(x+1)
dgs=gs.diff(x,1).simplify()
gn=S.lambdify(x,gs,'numpy') #las pasamos a numérico
dgn=S.lambdify(x,dgs,'numpy')
a,b=(0,2) #como vemos puede que no converge hasta 0,8, a partir de ahí nos aseguramos
X=N.linspace(a,b)
fig=plt.figure(figsize=(8,6))
plt.subplot(2,1,1)
plt.plot(X,gn(X),[a,b],[a,b])
plt.grid()
plt.ylabel(r'$g\left(x\right)$')
plt.subplot(2,1,2)
plt.plot(X,gn(X),[a,b],[-1,-1])
plt.plot(X,gn(X),[a,b],[1,1])
plt.plot(X,dgn(X))
plt.grid()
plt.ylabel(r'$g^\prime\left(x\right)$')
plt.show()

#g2
a,b=(1,1.45)
gs2=(S.ln(4./x))
dgs2=gs2.diff(x,1).simplify()
gn2=S.lambdify(x,gs2,'numpy')
dgn2=S.lambdify(x,dgs2,'numpy')
fig=plt.figure(figsize=(8,6))
plt.subplot(2,1,1)
plt.plot(X,gn2(X),[a,b],[a,b])
plt.grid()
plt.ylabel(r'$g\left(x\right)$')
plt.subplot(2,1,2)
plt.plot(X,gn2(X),[a,b],[-1,-1])
plt.plot(X,gn2(X),[a,b],[1,1])
plt.plot(X,dgn2(X))
plt.grid()
plt.ylabel(r'$g^\prime\left(x\right)$')
plt.show()

#g3
a,b=(0,2)
gs3=(4*S.exp(-x))
dgs3=gs3.diff(x,1).simplify()
gn3=S.lambdify(x,gs3,'numpy')
dgn3=S.lambdify(x,dgs3,'numpy')
fig=plt.figure(figsize=(8,6))
plt.subplot(2,1,1)
plt.plot(X,gn2(X),[a,b],[a,b])
plt.grid()
plt.ylabel(r'$g\left(x\right)$')
plt.subplot(2,1,2)
plt.plot(X,gn3(X),[a,b],[-1,-1])
plt.plot(X,gn3(X),[a,b],[1,1])
plt.plot(X,dgn3(X))
plt.grid()
plt.ylabel(r'$g^\prime\left(x\right)$')
plt.show()