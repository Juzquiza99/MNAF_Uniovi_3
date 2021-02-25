# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:57:56 2019

@author: UO264982
"""

import numpy as np
import numpy.linalg as la



#PROGRAMA EN EL QUE LE INDICAMOS EL MÉTODO QUE QUEREMOS SEGUIR (JACOBI, GAUSS Y RELAJACIÓN)

def sist(met,a,b, w):
    ad=np.diag(np.diag(a))
    au=-np.triu(a,1)
    al=-np.tril(a,-1)
    if met[0].lower()=='j': #JACOBI
        k=np.dot(la.inv(ad),(al+au))
        d=np.dot(la.inv(ad),b)

    elif met[0].lower()=='g': #GAUSS SIEDEL
        k=np.dot(la.inv(ad-al),au)
        d=np.dot(la.inv(ad-al),b)

    elif met[0].lower()=='r': #RELAJACIÓN
        k=np.dot(la.inv(ad-w*al),(1-w)*ad+w*au)
        v=ad-w*al
        d=np.dot(w*(la.inv(v)),b)
    return[k,d]
               
                
#A=np.random.randint(10,size=(5,5))
#B=np.random.randint(10,size=(5,))
#print(sist('j',A,B))

E=np.array([[1,2,-2],[1,1,1],[2,2,1]])
F=np.array([1,3,5])
print(sist('j',E,F,0.2))
print(sist('g',E,F,0.2))
print(sist('r',E,F,0.2))

#Calculamos la norma y el radio espectral
#Radio espectral: supremos de los valores propios
h=sist('r',E,F,0.2)

#Creamos dos funciones para la norma y el radio espectral
def norma(x):
    nor=la.norm(x)
    return nor

def radesp(x):
    val=la.eigvals(x)
    valsup=max(np.abs(val))
    return valsup

print (norma(h[0]))
print (radesp(h[0]))


#Mecánica estructural
a,b, c, d=(np.pi/6, np.pi/3, 10000, np.pi/2)
#Orden incógnitas: f1, f2, f3, h1, v1, v2
G=np.zeros((6,6))
G[0,[0,2]]=[np.cos(a),-np.cos(b)]
G[1,[0,2]]=[np.sin(a), np.sin(b)]
G[2,[3,0,1]]=[1, -np.cos(a), -1]
G[3,[4,0]]=[1,-np.sin(a)]
G[4,[1,2]]=[1,np.cos(b)]
G[5,[5,2]]=[1,-np.sin(b)]
print(G)
H=np.array([c*np.cos(d), c*np.sin(d),0,0,0,0])

print(sist('j',G,H,0.2))
print(sist('g',G,H,0.2))
print(sist('r',G,H,1.5))


#Reparto de recursos

M=np.array([[3,4,7,20],[20,25,40,50],[10,15,20,22],[10,8,20,15]])
N=np.array([1706,2065,3474,4616])
p=sist('j',M,N,0.2)
q=sist('g',M,N,0.2)
t=sist('r',M,N,0.2)
print(p)
print(q)
print(t)
print(norma(p[0]))
print (radesp(q[0]))