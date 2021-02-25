# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:15:39 2019

@author: UO264982
"""

#INTEGRACIÓN 1

import sympy as S
import numpy as N
import numpy.linalg as la

n,x,y=S.symbols('n x y',real=True)
s0 = S.integrate(S.cos(3*n+x), x)
s1 = S.integrate(S.cos(x**2), (x,0,S.pi/2))
s2 = S.integrate(S.exp(-x),(x,0,S.oo))
print(s0,s1,s2)
s3 = S.integrate(S.exp(-x**2 - y**2), (x, -S.oo, S.oo), (y, 0, S.oo))
print(s3)

#MÉTODO DE COEF. INDETERMINADOS:
#resolver el sistema Ax=b, tal que las filas de A son los puntos del soporte elevados a el numero de la fila -1
#las filas de B son 1/n (b^n-a^n)
def met_coef_indet(a,b,xk,tol):
    #calculamos los coeficientes primero
    intervalo=N.array([a,b])
    n=len(xk)
    A=N.ones((n,n))
    B=N.ones(n)
    #definimos otro para que ocupe otro sitio de memoria que no sea el de intervalo
    #para que no cambien a la vez
    tmp=N.array([a,b]) 
    for i in range(n):
        if i==0:
            A[i,:]=A[i,:]
            B[i]=tmp[1]-tmp[0]
        else:
            tmp*=intervalo
            A[i,:]=xk*A[i-1,:]
            B[i]=(tmp[1]-tmp[0])/(i+1)
    coeficientes=N.linalg.solve(A,B)
    
    #Ahora vemos el orden
    tmpA=A[-1]
    orden=n-1
    tmp*=intervalo
    tmpA*=xk
    exacta=(tmp[1]-tmp[0])/(orden+2)
    formula=N.dot(tmpA,coeficientes)
    
    while abs(exacta-formula)<tol:
        orden+=1
        tmp*=intervalo
        tmpA*=xk
        exacta=(tmp[1]-tmp[0])/(orden+2)
        formula=N.dot(tmpA,coeficientes)
    
       
    return [coeficientes, orden]

sop1=[1./4,1./2,3./4]
sop2=[0.5,0.75,1]
sop3=[0,1,2]
sop4=[-1,0,1]
print(met_coef_indet(0.25,0.75,sop1,1E-5))
print(met_coef_indet(0.5,1,sop2,1E-5))
print(met_coef_indet(0,2,sop3,1E-5))
print(met_coef_indet(-1,1,sop4,1E-5))