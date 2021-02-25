# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:42:03 2019

@author: UO264982
"""

#APROXIMACIÓN DISCRETA
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt




def aproxmc1d(base,x,y,fun):#fun es solo para calcular el error
    n=len(base)
    m=len(x)
    X=np.zeros((n,m))
    f=np.zeros(n)
    coef=np.zeros(n)
    
    for i in range(n):
        X[i]=base[i](x)
        
    G = np.dot(X,np.transpose(X))
    f = np.dot(X,y)
    coef=la.solve(G,f)
    
    primero=np.dot(y,y)
    segundo=np.dot(coef,f)
    tercero=np.sum(np.outer(coef.T,coef)*G)
    EC=primero-2*segundo+tercero
    ECM=EC/len(x)
    S=np.sqrt(EC/(len(x)-len(coef)))
    
        
    return G,f,coef,EC,ECM,S


base1=[lambda x: np.ones_like(x), lambda x: 1./x, lambda x: np.sqrt(x)]
fun1=lambda x: 1./(1+x**2)
 
ptos=np.linspace(1,5,20)
yptos=fun1(ptos)
   
base2=[lambda x: np.ones_like(x), lambda x:x, lambda x: x**2]
base3=[lambda x: np.ones_like(x), lambda x: np.cos(x), lambda x: np.sin(x)]

solu1=aproxmc1d(base1,ptos,yptos,fun1)
solu2=aproxmc1d(base2,ptos,yptos,fun1)
solu3=aproxmc1d(base3,ptos,yptos,fun1)

G1,f1,coef1,EC1,ECM1,S1=solu1
G2,f2,coef2,EC2,ECM2,S2=solu2
G3,f3,coef3,EC3,ECM3,S3=solu3


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
print(sist1)

Y1=sist1[0]*base1[0](ptos)+sist1[1]*base1[1](ptos)+sist1[2]*base1[2](ptos)
Y2=sist2[0]*base2[0](ptos)+sist2[1]*base2[1](ptos)+sist2[2]*base2[2](ptos)
Y3=sist3[0]*base3[0](ptos)+sist3[1]*base3[1](ptos)+sist3[2]*base3[2](ptos)

plt.figure(1)
plt.plot(ptos,Y1)
plt.plot(ptos,Y2)
plt.plot(ptos,Y3)
plt.show()
