# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:34:42 2019

@author: javie
"""

import numpy as np
import numpy.linalg as la

def cholesky(A):
    fA,cA=A.shape
    print(A.shape)
    x=np.zeros_like(A,dtype=float)
    for i in range(fA):
        for j in range(i+1):
            for k in range(j+1):
                suma=x[i,k-1]*x[j,k-1]
                if i==j:
                    x[i,j]=np.sqrt(A[i,i]-suma)
                else:
                    x[i,j]=(1./x[j,j])*(A[i,j]-suma)
    return(x)
    
A=np.array([[6,3,4,8],[3,6,5,1],[4,5,10,7],[8,1,7,25]])
print(cholesky(A))    
    
    
print(la.cholesky(A))