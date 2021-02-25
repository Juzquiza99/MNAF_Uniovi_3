# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:27:46 2019

@author: javie
"""

import numpy as np

def slgaussjordan(A,b):
    A=A.astype(float)
    b=b.astype(float)
    x=np.zeros_like(b,dtype=float)
    fA, cA = A.shape
    for i in range(fA):
        if A[i,i]==0:
            raise ValueError('pivot becomes null')
        for j in range(fA):
            if j!=i:
                m=-A[j,i]/A[i,i]
                A[j,i+1:]=A[j,i+1:]+m*A[i,i+1:]
                b[j]=b[j]+m*b[i]
                A[j,i]=0
    print(A)       
    x=soldiag(A,b)
    return x
A=np.array([[1,2,3],[4,9,7],[5,6,8]])
B=np.array([1,2,4])
print('Solución del sistema')
print(slgaussjordan(A,B))