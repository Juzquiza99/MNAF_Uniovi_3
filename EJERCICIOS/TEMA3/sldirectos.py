# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:10:28 2019

@author: UO264982
"""

import numpy as np
import numpy.linalg as la

A=np.random.randint(10,size=(5,5))
B=np.random.randint(10,size=(5,))
print(A)
print(B)

#MATRIZ DIAGONAL: solución de un sistema de ecuaciones (A.x=C), tal que A
#es una matriz diagonal

def soldiag(A,B):
    diago=np.diag(A)
    fA, cA = A.shape
    b=A-np.diag(diago)
    if fA != cA:
        raise ValueError('A no es una matriz cuadrada')
        if b.any():
            raise ValueError('A no es una matriz diagonal')
    if not diago.all():
        raise ValueError('A es una matriz singular')
    if len(B.shape) != 1:
        raise ValueError('B no es un vector')
    if fA != B.shape[0]:
        raise ValueError('No coinciden la matriz A y el vector B')
    return B/diago

print('Matriz diagonal')

C = np.diag(np.diag(A))
print (soldiag(C,B))
soldiasol=la.solve(C,B)
print(soldiasol)

#MATRIZ TRIANGULAR SUPERIOR: solución de un sistema de ecuaciones (A.x=C),
#tal que A es una matriz triangular superior

print('Matriz triangular superior')
def sltris(A,B):
    diago=np.diag(A)
    fA, cA = A.shape
    if fA != cA:
        raise ValueError('A no es una matriz cuadrada')
    if fA != B.shape[0]:
        raise ValueError('No coinciden la matriz A y el vector B')
    if not diago.all():
        raise ValueError('A es una matriz singular')
        
    x=np.zeros_like(B,dtype=float)
    for k in np.arange(fA-1,-1,-1):
        suma=np.dot(A[k,k+1:],x[k+1:])
        x[k]=(B[k]-suma)/A[k,k]
    return A, x
   
D=np.triu(A)   
print (sltris(D,B))
soltris=la.solve(D,B)
print (soltris)


#MATRIZ TRIANGULAR INFERIOR: solución de un sistema de ecuaciones (A.x=C),
#tal que A es una matriz triangular inferior


def sltrinf(A,B):
    diago=np.diag(A)
    fA, cA = A.shape
    if fA != cA:
        raise ValueError('A no es una matriz cuadrada')
    if len(B.shape) != 1:
        raise ValueError('B no es un vector')
    if fA != B.shape[0]:
        raise ValueError('No coinciden la matriz A y el vector B')
    if not diago.all():
        raise ValueError('A es una matriz singular')
        
    x=np.zeros_like(B,dtype=float)
    for k in np.arange(fA):
        suma=np.dot(A[k,:k],x[:k])
        x[k]=(B[k]-suma)/A[k,k]
    return A,x
    
print('Matriz triangular inferior:')
E=np.tril(A)
print(sltrinf(E,B))
soltrinf=la.solve(E,B)
print(soltrinf)


#MÉTODO GAUSS

def slgauss(A,b):
    A=A.astype(float)
    b=b.astype(float)
    x=np.zeros_like(b,dtype=float)
    fA, cA = A.shape
    for i in range(fA):
        if A[i,i]==0:
            raise ValueError('pivot becomes null')
        for j in range(i+1,fA):
            m=A[j,i]/A[i,i]
            A[j,i+1:]=A[j,i+1:]-m*A[i,i+1:]
            b[j]=b[j]-m*b[i]
            A[j,i]=0
    x=sltris(np.triu(A),b)
    return x

print('Método de Gauss')
print(slgauss(A,B))

def slgauss2(A,b):
    A=A.astype(float)
    b=b.astype(float)
    x=np.zeros_like(b,dtype=float)
    fA, cA = A.shape
    for i in range(fA):
        if A[i,i]==0:
            raise ValueError('pivot becomes null')
        for j in range(i+1,fA):
            m=A[j,i]/A[i,i]
            A[j,i+1:]=A[j,i+1:]-m*A[i,i+1:]
            b[j]=b[j]-m*b[i]
            A[j,i]=m
    x=sltris(np.triu(A),b)
    return x, A
print('Método de Gauss sin buscar hacer ceros')
G=np.random.randint(-5,5,size=(5,5))
G=G.astype(float)
print(slgauss2(G,B))


#Gauss con pivote simple
def slgauss3(A,b):
    A=A.astype(float)
    b=b.astype(float)
    x=np.zeros_like(b,dtype=float)
    fA, cA = A.shape
    for i in range(fA):
        valor=max(abs(A[i:,i]))
        if valor==0:
            raise ValueError('pivot becomes null')
            
        pos=np.argmax(abs(A[i:,i]))
        if pos !=0:
            A[[i,i+pos],:]=A[[i+pos,i],:]
        for j in range(i+1,fA):
            m=A[j,i]/A[i,i]
            A[j,i+1:]=A[j,i+1:]-m*A[i,i+1:]
            b[j]=b[j]-m*b[i]
            A[j,i]=m
    x=sltris(np.triu(A),b)
    return x, A

print('Método de Gauss con pivote simple')
Z=np.array([[2,1,3],[-5,-3,6],[3,-3,1]])
Y=np.random.randint(10,size=(3,))
J=np.array([[0,1,4,5,6],[7,5,4,2,8],[9,0,5,4,3],[9,5,6,0,5],[7,4,3,2,6]])
print(slgauss3(J,B))
