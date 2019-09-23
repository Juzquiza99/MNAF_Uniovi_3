# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np

def aleatorio(n,x0,a,b):
    x=np.zeros(n+1)
    x[0]=x0

    for i in range(n):
        x[i+1]=np.mod(a*x[i]+b,n)
        
    print (x)
    
lista=aleatorio(10,5,1,3)

print(lista)

#def genera(xo,a,x,m)