# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:14:01 2019

@author: UO264931
"""

import numpy as np
import scipy.integrate as SI

'''    
    for i in range(1,n):
        #A[i:]=xk**(i) esta es válida pero no la vamos a usar
        A[i,:]=A[i-1,:]*xk
        B[i]=(intervalo[1]-intervalo[0])/(i+1)
        intervalo*=intervalo
    coeficientes=np.linalg.solve(A,B)
'''  

#es la matriz de vandermonde al parecer, pero cambiada
tol=1E-9

def metodo_coeficientes_indeterminados(a,b,xk,tol):
    #calculamos los coeficientes primero
    intervalo=np.array([a,b])
    n=len(xk)
    A=np.ones((n,n))
    B=np.ones(n)
    #definimos otro para que ocupe otro sitio de memoria que no sea el de intervalo
    #para que no cambien a la vez
    tmp=np.array([a,b]) 
    for i in range(n):
        if i==0:
            A[i,:]=A[i,:]
            B[i]=tmp[1]-tmp[0]
        else:
            tmp*=intervalo
            A[i,:]=xk*A[i-1,:]
            B[i]=(tmp[1]-tmp[0])/(i+1)
    coeficientes=np.linalg.solve(A,B)
    
    #Ahora vemos el orden
    tmpA=A[-1]
    orden=n-1
    tmp*=intervalo
    tmpA*=xk
    exacta=(tmp[1]-tmp[0])/(orden+2)
    formula=np.dot(tmpA,coeficientes)
    
    while abs(exacta-formula)<tol:
        orden+=1
        tmp*=intervalo
        tmpA*=xk
        exacta=(tmp[1]-tmp[0])/(orden+2)
        formula=np.dot(tmpA,coeficientes)
    
       
    return [coeficientes, orden]

#prueba y prueba3 deberian dar lo mismo   

prueba=np.array([1/4,1/2,3/4])
print(metodo_coeficientes_indeterminados(0,1,prueba,tol))

prueba3=np.array([5/4,6/4,7/4])
print(metodo_coeficientes_indeterminados(1,2,prueba3,tol))

print('\n')
#prueba 2 y solu2 deberian dar los mismo

prueba2=np.array([1,3/2,2])
print(metodo_coeficientes_indeterminados(1,2,prueba2,tol))
solu2=np.array([1/6,4/6,1/6])
print(solu2)      

'''
print('\n')
print('Vemos que los coeficientes no dependen de los puntos si no de su separación, los siguientes deberían salir iguales')
prueba31=np.array([0,1,2])
prueba32=np.array([-1,0,1])
prueba33=np.array([10,11,12])

print(metodo_coeficientes_indeterminados(0,1,prueba31,tol))
print(metodo_coeficientes_indeterminados(0,1,prueba32,tol))
print(metodo_coeficientes_indeterminados(0,1,prueba33,tol))
'''    