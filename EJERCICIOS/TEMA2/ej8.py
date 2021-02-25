# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:04:41 2019

@author: javie
"""

import numpy as np
import matplotlib.pyplot as plt
#EJERCICIO 8

def func(ro):
    return [1,-3,0,4*ro]
dens=np.linspace(0.05,0.95,20)
hund=np.zeros_like(dens)

for i in range(len(dens)):
    parametros=func(dens[i])
    raices=np.roots(parametros)
    raiz=list(filter(lambda x: x<=2 and x>=0, raices))
    hund[i]=raiz[0]
print (hund,raices)


plt.figure()
plt.plot(dens, hund/2)
plt.grid()
