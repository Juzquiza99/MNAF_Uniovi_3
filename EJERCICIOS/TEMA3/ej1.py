# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:00:15 2019

@author: javie
"""
import numpy as np

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
            return abso,suma[0,:]   
            
A=np.array([[-3,20,-10,10],[-4,-25,15,8],[-7,40,-20,20],[-20,50,22,15]])
print (A)

print(norma('1',A))