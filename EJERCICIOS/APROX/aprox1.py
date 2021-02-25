# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

#APROXIMACIÓN CONTINUA
import numpy as np
import scipy.integrate as si
import numpy.linalg as la
import matplotlib.pyplot as plt

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
    
    
base1=[lambda x: np.ones_like(x), lambda x: 1./x, lambda x: np.sqrt(x)]
fun1=lambda x: 1./(1+x**2)

base2=[lambda x: np.ones_like(x),lambda x:x, lambda x: x**2]
base3=[lambda x: np.ones_like(x), lambda x: np.cos(x), lambda x: np.sin(x)]
solu1=aproxmc1c(base1,1,5,fun1)
solu2=aproxmc1c(base2,1,5,fun1)
solu3=aproxmc1c(base3,1,5,fun1)

print('G:')
print(solu1[0])

print('f:')
print(solu1[1])
print('Coefs. c solución sistema')
sist1=la.solve(solu1[0],solu1[1])
print(sist1)

print('G:')
print(solu2[0])

print('f:')
print(solu2[1])

print('Coefs. c solución sistema')
sist2=la.solve(solu2[0],solu2[1])
print(sist1)

print('G:')
print(solu3[0])

print('f:')
print(solu3[1])

print('Coefs. c solución sistema')
sist3=la.solve(solu3[0],solu3[1])
print(sist3)

npts=201
a=1
b=5
X=np.linspace(a,b,npts)

Y1=sist1[0]*base1[0](X)+sist1[1]*base1[1](X)+sist1[2]*base1[2](X)
Y2=sist2[0]*base2[0](X)+sist2[1]*base2[1](X)+sist2[2]*base2[2](X)
Y3=sist3[0]*base3[0](X)+sist3[1]*base3[1](X)+sist3[2]*base3[2](X)

print(Y1)
error1=np.zeros(npts)
error2=np.zeros(npts)
error3=np.zeros(npts)
for i in range(npts):
    error1[i]=np.abs((fun1(X))[i]-Y1[i])
    error2[i]=np.abs((fun1(X))[i]-Y2[i])
    error3[i]=np.abs((fun1(X))[i]-Y3[i])

plt.figure(1)
plt.plot(X,Y1,label='base1')
plt.plot(X,error1,'go',label='error1')
plt.plot(X,Y2,label='base2')
plt.plot(X,error2,'bo',label='error2')
plt.plot(X,Y3,label='base3')
plt.plot(X,error3,'ro',label='error3')
plt.plot(X,fun1(X),'Función')
plt.grid()
plt.legend()
plt.show()
