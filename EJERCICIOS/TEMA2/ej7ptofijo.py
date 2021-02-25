# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:35:30 2019

@author: javie
"""
import numpy as N
#Ejerc 7 Pto fijo
def odenco(xn):#funcion para obtener el orden de converg de la sucesion
    for i in range(xn.shape[0]):
        pn=N.zeros
        pn[i]=N.log(abs((xn[i+2]-xn[i])/(xn[i+2]-xn[i+1])))/N.log(abs(((xn[i+2]-xn[i+1])/(xn[i+2]-xn[i]))))
    return pn[i]
    
print(odenco(resul[1]))