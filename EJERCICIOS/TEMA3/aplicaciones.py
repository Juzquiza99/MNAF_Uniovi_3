# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:10:08 2019

@author: UO264982
"""

import numpy as np
import numpy.linalg as la


#Aplicación I
A=np.array([[3,20,10,10],[4,25,15,8],[7,40,20,20],[20,50,22,15]])
print(A)
B=np.array([1706,2065,3474,4616])
print(B)

sol=la.solve(A,B) #Para solucionar el sistema
print(sol)

#Aplicación II
a,b, c, d=(np.pi/6, np.pi/3, 10000, np.pi/2)

#Orden incógnitas: f1, f2, f3, h1, v1, v2
F=np.zeros((6,6))
F[0,[0,2]]=[np.cos(a),-np.cos(b)]
F[1,[0,2]]=[np.sin(a), np.sin(b)]
F[2,[3,0,1]]=[1, -np.cos(a), -1]
F[3,[4,0]]=[1,-np.sin(a)]
F[4,[1,2]]=[1,np.cos(b)]
F[5,[5,2]]=[1,-np.sin(b)]
print(F)

C=np.array([c*np.cos(d), c*np.sin(d),0,0,0,0])
print (C)

solu=la.solve(F,C)
print(solu)