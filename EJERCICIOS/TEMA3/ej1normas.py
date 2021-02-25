# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:00:15 2019

@author: javier
"""
import numpy as np
import scipy.linalg as la

def norma(cual,A):
    fA,cA=A.shape
    print(A.shape)
    if cual==('1'):
        abso=np.array(A)
        suma=np.array(A)
        for i in range(fA):
            for j in range(cA):
                abso[:,:]=abs(A[:,:])
                suma[:,j]=np.sum(abso[:,j])
            return abso,suma[0,:],max(suma[0,:])   
    
    elif cual==('2'):
        if fA!=cA:
            raise ValueError('La matriz ha de ser cuadrada')
        else:
            auto=la.eig(A)
            ro= np.max(auto[0])
            return np.sqrt(np.dot(A, A.T)*ro)
                
    elif cual==('inf'):
        return np.max(np.sum(abs(A), axis=1)) #filas (axis=0: columnas)         
                
A=np.array([[4,-5,4,-1],[4,-2,-2,2],[2,-2,-4,-1]])
print (A)
B=np.random.randint(5,size=(3,3))
print(norma('inf',A))